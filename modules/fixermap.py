import sys
def tovariable(v):
	v=v.strip()
	v=v.rstrip()
	v=v.lower()
	k=v.split(" ")
	ret=""
	for a in k:
		ret+=a
	return ret
def replacePred(l):
	st=""
	while (len(l)):
		v =l.find("?")
		if (v!=-1):
			st+=l[0:v]
			if (l>0):
				if (v==len(l)-1):
					st+="?"
				elif (v==len(l)-2):
					st+="?"
				else:
					#print l[v-2:v+2]
					if (l[v+1]==' ' and l[v+2]==l[v+2].capitalize()):
						st+="..."
					elif (l[v+1]==' '):
						st+=","
					else:
						st+="'"
			l=l[v+1:]
		else:
			st+=l
			l=""
		
	return st
def AddQuoth(l):
	w=l.find(": ")
	if (w==-1 or w>=len(l)-3):
		return l
	else:
		return (l[0:w],l[w+2:])
def processText(l):
	l=replacePred(l)
	return [AddQuoth(l)]

def AddVar(m,k,v):
	if k in m:
		m[k]+=v;
	else:
		m[k]=v
def fixupMap(s):
	where=s.find("'failure'")
	if (where==-1):
		where=s.find('"failure"')
	ret=s[0:where+len("'failure'")]
	early=s[where+len("'failure'"):]
	where=early.find(",")
	val=early[0:where]
	val=val.replace("'","")
	val=val.replace('"',"")
	ret+=val+early[where:]
	return ret
	
def NoNumber(var):
	var=var.replace("0","");
	var=var.replace("1","");
	var=var.replace("2","");
	var=var.replace("3","");
	var=var.replace("4","");
	var=var.replace("5","");
	var=var.replace("6","");
	var=var.replace("7","");
	var=var.replace("8","");
	var=var.replace("9","");
	return var
for a in sys.argv[1:]:
	f=open(a)
	lines = f.readlines()
	stage=0
	m={}
	var="fixer = "
	for l in lines:
		if (len(l) and l!='\n'):
			l=l.strip()
			l=l.rstrip()
			if stage==0:
				if (len(m)):
					print var+" = "+ fixupMap(str(m))
				var= tovariable(l)			
				m={}
				stage=1
			elif stage==1:
				if (l.find("Accept")==0):
					stage=2
					m["failure"]=NoNumber(var)+"failure"
				else:
					AddVar(m,"intro",processText(l))
			elif stage==2:
				if (l.find("Reject")==0):
					stage=3
				else:
					AddVar(m,"accept",processText(l))
			elif stage==3:
				AddVar(m,"reject1",processText(l))
			elif stage==4:
				if (l.find("Accept")==0):
					stage=5
				else:
					AddVar(m,"reconsider",processText(l))
			elif stage==5:
				if(l.find("Reject")==0):
					stage=6
			elif stage==6:
				AddVar(m,"reject2",processText(l))
			elif stage==7:
				if (l.find("Accept")==0):
					stage=8
				else:
					AddVar(m,"reminder",processText(l))
			elif stage==8:
				if (l.find("Fly")==0):
					stage=0
		elif (l=='\n'):
			if (stage==3):
				stage=4
			if (stage==6):
				stage=7
	print var+" = "+fixupMap(str(m))
			
			
		
