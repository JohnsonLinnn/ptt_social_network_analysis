#imoprt libaries
import networkx as nx
import json
  
# Opening JSON file
f = open('./LivingGoods-1-30.json','r', encoding='UTF-8')
data = json.load(f)
data =data['articles']
#create containers
node_check={}
node_container=[] 
edge_container=[]


#function of update node
def update_node(post_obj,nodes_dict,userid,type):
    if nodes_dict.get(userid)==None:
        if type =='posts':
            nodes_dict[userid]={
                'posts':1,
                'comments':0,
                'articles':post_obj['article_title']
            }
            
        elif type=='comments':
            nodes_dict[userid]={
                'posts':0,
                'comments':1,
                'articles':[]
                
            }
    else :
        nodes_dict[userid][type]=nodes_dict[userid][type]+1
        if type=='post':
            nodes_dict[userid]['articles'].append(post_obj['article_title'])

#function1 create author's node 
def create_nodes(obj):
    print(counter)
    counter 
    #check if obj's author exist
    if(obj['author']!=None and '發錢' not in obj['article_title']):
        #get the cleaned user ID
        sep = ' '
        author_cleaned_id=obj['author'].split(sep, 1)[0]
        update_node(obj,node_check,author_cleaned_id,'posts')
        create_comments_node_and_edge(obj,author_cleaned_id,edge_container)

#function2 create comment's node along with the edges
def create_comments_node_and_edge(obj,author_id,edges_container):
    edge_check={}
    list_of_push_id=obj['push']

    for j in list_of_push_id:
        a=str(author_id)+str(j)
        #creating edge
        if(author_id!=j) and (edge_check.get(a)==None):
            edges_container.append([author_id,j])
            edge_check[a]=True
        #check if commenter exist
        update_node(obj,node_check,j,'comments')
counter=1
for i in data:
    
    create_nodes(i)
    counter+=1

f.close()         
""" Create a graph with three nodes"""
G = nx.MultiGraph()

for key,value in node_check.items():
    G.add_node(key,postcount=value['posts'],replycount=value['comments'],articles=value['articles'])
for i in edge_container:
    G.add_edge(i[0],i[1])
nx.write_gexf(G, "Living_Good_filtered.gexf", version="1.2draft")

