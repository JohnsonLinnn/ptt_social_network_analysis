#imoprt libaries
import networkx as nx
import json
  
# Opening JSON file
f = open('./gossiping-1-433.json','r', encoding='UTF-8')

node_check={}
node_container=[] 

edge_container=[]

data = json.load(f)
data =data['articles']
x=0
for i in data:
    print(x)
    x+=1
    sep = ' '
    cleaned_author_ID =i['author'].split(sep, 1)[0]
    list_of_push_id=i['push']
    #check if author exist 
    if(node_check.get(cleaned_author_ID )==None):
        node_check[cleaned_author_ID]={
            'posts':1,
            'comments':0
        }
    else:
        node_check[cleaned_author_ID]['posts']=node_check[cleaned_author_ID]['posts']+1  
    #check if the push author exist 
    edge_check={}    
    for j in list_of_push_id:
        a=str(cleaned_author_ID)+str(j)
        #creating edge
        if(cleaned_author_ID!=j) and (edge_check.get(a)==None):
            edge_container.append([cleaned_author_ID,j])
            edge_check[a]=True
        #check if commenter exist
        if(node_check.get(j)==None):
            node_check[j]={
            'posts':0,
            'comments':1
        }
        else:
            node_check[j]['comments']=node_check[j]['comments']+1
#{'userID':{post_count:x,reply_count}}

# Closing file
f.close()         
""" Create a graph with three nodes"""
G = nx.MultiGraph()

for key,value in node_check.items():
    G.add_node(key,postcount=value['posts'],replycount=value['comments'])
for i in edge_container:
    G.add_edge(i[0],i[1])
nx.write_gexf(G, "433_page_gossiping.gexf", version="1.2draft")