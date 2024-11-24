#join two set

loopset = {'apple','orange','berry'}
loopset2 = {'cherry','banana','tomata'}
loopset3 = loopset.union(loopset2)
#print(loopset3)





#multiple set  join

loopset = {'apple','orange','berry'}
loopset2 = {'cherry','banana','tomata'}
loopset3 = {'lichu','mango','nut'}
loopset4 = {'watermelon','grape','jackfruit'}

loopset5 = loopset | loopset2 | loopset3 | loopset4
#print(loopset5)




#set intersection
loopset = {'apple','orange','berry'}
loopset2 = {'cherry','banana','tomata','orange'}
loopset6 = loopset.intersection(loopset2)
print(loopset6)