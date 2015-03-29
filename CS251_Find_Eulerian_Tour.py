# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    d=[]
    find(graph, d)        
    return d

def find(graph,p):
    if not graph:
        return

    i=0
    while i<len(graph):
        if not p:
            g=[]
            g.append(graph[i][0])
            g.append(graph[i][1])
            gr=list(graph)
            gr.pop(i)
            find(gr,g)
            if len(g)==len(graph)+1:
                p[0:0]=g
                return
            else:
                g=[]
                g.append(graph[i][1])
                g.append(graph[i][0])
                gr=list(graph)
                gr.pop(i)
                find(gr,g)
                if len(g)==len(graph)+1:
                    p[0:0]=g
                    return

        else:
            last=len(p)-1
            if graph[i][0]==p[last]:
                g=[]
                g.append(graph[i][1])
                gr=list(graph)
                gr.pop(i)
                find(gr,g)

                if len(g)==len(gr)+1:
                    p[len(p):len(p)]=g
                    return
            elif graph[i][1]==p[last]:
                g=[]
                g.append(graph[i][0])
                gr=list(graph)
                gr.pop(i)
                find(gr,g)

                if len(g)==len(gr)+1:
                    p[len(p):len(p)]=g
                    return

        i+=1
    return


print find_eulerian_tour([(1, 2), (3, 1) ,(2, 3)])
