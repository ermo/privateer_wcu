uniform int light_enabled[gl_MaxLights];
uniform int max_light_enabled;
uniform sampler2D diffuseMap;
uniform sampler2D envMap;
uniform sampler2D specMap;
uniform sampler2D glowMap;
uniform sampler2D normalMap;
uniform sampler2D damageMap;
uniform sampler2D detail0Map;
uniform sampler2D detail1Map;
uniform vec4 cloaking;
uniform vec4 damage;
uniform vec4 envColor;

vec3 matmul(vec3 tangent, vec3 binormal, vec3 normal,vec3 lightVec) {
  return vec3(dot(lightVec,tangent),dot(lightVec,binormal),dot(lightVec,normal));
}
vec3 imatmul(vec3 tangent, vec3 binormal, vec3 normal,vec3 lightVec) {
  return lightVec.xxx*tangent+lightVec.yyy*binormal+lightVec.zzz*normal;
}

vec2 EnvMapGen(vec3 f) {
   float fzp1=f.z+1.0;
   float m=2.0*sqrt(f.x*f.x+f.y*f.y+(fzp1)*(fzp1));
   return vec2(f.x/m+.5,f.y/m+.5);
}

float bias(float f){ return f*0.5+0.5; }
vec2  bias(vec2 f) { return f*0.5+vec2(0.5); }
vec3  bias(vec3 f) { return f*0.5+vec3(0.5); }
vec4  bias(vec4 f) { return f*0.5+vec4(0.5); }

float expand(float f){ return f*2.0-1.0; }
vec2  expand(vec2 f) { return f*2.0-vec2(1.0); }
vec3  expand(vec3 f) { return f*2.0-vec3(1.0); }
vec4  expand(vec4 f) { return f*2.0-vec4(1.0); }

float lerp(float f, float a, float b){return (1.0-f)*a+f*b; }
vec2  lerp(float f, vec2 a, vec2 b) { return (1.0-f)*a+f*b; }
vec3  lerp(float f, vec3 a, vec3 b) { return (1.0-f)*a+f*b; }
vec4  lerp(float f, vec4 a, vec4 b) { return (1.0-f)*a+f*b; }

float spec2lingloss( in vec4 spec_col )
{
  vec2 temp = spec_col.rg;
  temp *= temp;
  return (temp.r+temp.g)*0.5;
}
float shininessMap( in float lin_gloss )
{
    float temp1 = (1.0625+lin_gloss) / (1.0625-lin_gloss);
    float temp2 = temp1 * temp1 * temp1;
    return (temp2*477.0) / (temp2+477.0);
}
float shininess2Lod( in float lin_gloss )
{
    float temp1 = lin_gloss * lin_gloss * lin_gloss + 1.07;
    float temp2 = 0.92 - lin_gloss;
    return temp1 * temp2 * 15.2 + lin_gloss * 8.5 - 5.0;
}
void lightingLight(
   in vec3 light, in vec3 normal, in vec3 vnormal, in vec3 eye, in vec3 reflection, 
   in vec4 lightDiffuse, in float lightAtt, 
   in vec4 diffusemap, in vec3 spec_col, in float shininess,
   in vec4 ambientProduct,
   inout vec3 diffuse, inout vec3 specular)
{
   float VNdotLx4= clamp( 4.0 * dot(vnormal,light), 0.0, 1.0 );
   float NdotL = clamp( dot(normal,light), -1.0, VNdotLx4 );
   float RdotL = clamp( dot(reflection,light), 0.0, VNdotLx4 );
   float s = 1.0 - (NdotL*NdotL);
   float temp = clamp( NdotL - (0.94 * s * s * s * s * NdotL) + 0.005, 0.0, 1.01 ); //soft penumbra
   specular += ( pow( RdotL, shininess ) * shininess * lightDiffuse.rgb );
   diffuse  += ( temp * lightDiffuse.rgb );
   //specular += pow(clamp(RdotL*8.0-7.0,0.0,1.0),0.25);
   //diffuse  += pow(clamp(NdotL*8.0-7.0,0.0,1.0),0.25);
}

#define lighting(name, lightno_gl, lightno_tex) \
void name( \
   in vec3 normal, in vec3 vnormal, in vec3 eye, in  vec3 reflection, \
   in vec4 diffusemap, in vec3 spec_col, in float shininess, \
   inout vec3 diffuse, inout vec3 specular) \
{ \
   lightingLight( \
      normalize(gl_TexCoord[lightno_tex].xyz), normal, vnormal, eye, reflection, \
      gl_FrontLightProduct[lightno_gl].diffuse, \
      gl_TexCoord[lightno_tex].w, \
      diffusemap, spec_col, shininess, \
      gl_FrontLightProduct[lightno_gl].ambient, \
      diffuse, specular); \
}

lighting(lighting0, 0, 5)
lighting(lighting1, 1, 6)

vec3 lightingClose(in vec3 diffuse, in vec3 specular, in vec4 diffusemap, in vec3 spec_col )
{
   return (diffuse*diffusemap.rgb) + (specular*spec_col);
}

vec3 envMapping(in vec3 reflection, in float glossLOD, in vec3 spec_col)
{
   return texture2DLod(envMap, EnvMapGen(reflection), glossLOD).rgb * spec_col * vec3(2.0);
}

vec3 ambMapping(in vec3 normal, in vec3 diff_col)
{
   return texture2DLod(envMap, EnvMapGen(normal), 7.0).rgb * diff_col;// * vec3(2.0);
}

void main() 
{
  vec2 texcoords2 = gl_TexCoord[0].xy;
  // Retrieve normals
  vec3 iNormal=gl_TexCoord[1].xyz;
  vec3 iTangent=gl_TexCoord[2].xyz;
  vec3 iBinormal=gl_TexCoord[3].xyz;
  vec3 vnormal=iNormal;
  vec3 normal=normalize(imatmul(iTangent,iBinormal,iNormal,expand(texture2D(normalMap,gl_TexCoord[0].xy).wyz)));
  
  // Other vectors
  vec3 eye = gl_TexCoord[4].xyz;
  vec3 reflection = -reflect(eye,normal);
  
  // Init lighting accumulators
  vec3 diffuse = vec3(0.0);
  vec3 specular= vec3(0.0);
  
  // Sample textures
  vec4 damagecolor = texture2D(damageMap , texcoords2 );
  vec4 diffusecolor= texture2D(diffuseMap, texcoords2 );
  vec4 speccolor   = texture2D(specMap   , texcoords2 );
  vec4 glowcolor   = texture2D(glowMap   , texcoords2 );
  
  //sanity enforcement:
  float temp = 1.0 - max( diffusecolor.r, max( diffusecolor.g, diffusecolor.b ) );
  speccolor.r = min( speccolor.r, temp );
  speccolor.g = min( speccolor.g, temp );
  speccolor.b = min( speccolor.b, temp );
  
  //When ao is baked into the diffuse, specular and glow textures, we put emissive alpha
  //in xmesh to 1.0; when ao is in glow.alpha, we put emissive alpha at 0.9 in xmesh.
  float ao_is_baked_in = 5.0*gl_FrontMaterial.emission.a-4.0;
  //Then, if the ao is already baked in, we get a value of 1.0 for ao, so it does nothing.
  float ao = max( glowcolor.a, ao_is_baked_in );
  
  //Fresnel:
  float alpha = diffusecolor.a * gl_FrontMaterial.diffuse.a;
  float fresnel_alpha = 1.0 - clamp( dot( eye, normal ), 0.0, 1.0 );
  alpha *= alpha;
  fresnel_alpha *= fresnel_alpha;
  alpha *= alpha;

  vec4 diffusemap  = lerp(damage.x, diffusecolor, damagecolor)*sqrt(ao);
  vec3 spec_col     = speccolor.rgb;
  spec_col.rgb     *= (1.0-damage.x);
  //gl_FrontMaterial.specular.a is used as a boolean: 1.0 means there's no shininess in alpha, so that
  //shininess should be computed from specular color using a (wrong), ad-hoc formula. 0.0 means that
  //the (probably wrong, as well, but maybe a bit less wrong) shininess is in specular's alpha channel.
  //Ergo the lerp. And we use the max of that or 1-alpha because transparent things should shine anyhow.
  float lin_gloss  = max(lerp( gl_FrontMaterial.specular.a, speccolor.a, spec2lingloss(speccolor) ),1.0-alpha);
  //gloss777 is a weird but intuitive name, in the sense that it conveys it's a large number, as opposed
  //to lin_gloss which is in the input range of 0-1.
  float gloss777   = shininessMap( lin_gloss );
  float glossLOD   = shininess2Lod( lin_gloss );
  
  fresnel_alpha = clamp( 0.1 + ( 0.9 * fresnel_alpha ), alpha, 1.0 );

  // Do lighting for every active light
  if (light_enabled[0] != 0)
     lighting0(normal, vnormal, eye, reflection, diffusemap, spec_col, gloss777, diffuse, specular);
  if (light_enabled[1] != 0)
     lighting1(normal, vnormal, eye, reflection, diffusemap, spec_col, gloss777, diffuse, specular);

  vec4 result;
  vec3 final_specular_color = lerp( alpha, vec3( fresnel_alpha ), spec_col )*ao*ao;

  result.a = fresnel_alpha;
  result.rgb  = lightingClose(diffuse, specular, diffusemap, final_specular_color)*sqrt(ao)
              + fresnel_alpha*glowcolor.rgb
              + (envMapping(reflection,glossLOD,final_specular_color)*fresnel_alpha)
              + ambMapping( normal, diffusemap.rgb*ao );
  result *= cloaking.rrrg;
  /*
  result = vec4(0.0);
  result.a  = 1.0;
  result.r  = clamp(dot(specular.rgb,vec3(1.0)),0.0,1.0);
  result.b  = clamp(dot(specular.rgb,vec3(1.0)),0.0,1.0);
  result.g  = clamp(dot(diffuse.rgb,vec3(1.0)),0.0,1.0);
  */
  gl_FragColor = result;
}
