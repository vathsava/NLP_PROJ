from jaccard import calcJaccard

filePath = "./developset/1999-W02-5.story"

f = open(filePath)
fr = f.read()
strings = fr.split('.')


quesPath = "./developset/1999-W02-5.questions"
f = open(quesPath)
questions = []
for line in f:
    if line.find("Question:") == 0:
        questions.append(line)
maxd=0;
ans="bbb";
for q in questions:
    for s in strings:
        f=calcJaccard(q, s);
        if maxd<f:
            ans=s;
            maxd=f;
    print q;
    print ans;
    maxd=0.0;
    ans="";
       



    
