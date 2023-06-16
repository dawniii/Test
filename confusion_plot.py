import numpy as np
import matplotlib.pyplot as plt
# classes = ['A','B','C','D','E']
# confusion_matrix = np.array([(9,1,3,4,0),(2,13,1,3,4),(1,4,10,0,13),(3,1,1,17,0),(0,0,0,1,14)],dtype=np.float64)


# 标签
# classes=[' 小斑病  ','大斑病',' 锈病','健康']
classes = ['0','1']
# 标签的个数
classNamber=2 #表情的数量

# 在标签中的矩阵
# confusion_matrix = np.array([[70  , 20 ],
#  [  17 , 105 ]],dtype=np.float64)
confusion_matrix = np.array([[70  , 20 ],
 [  17 , 105 ]])
plt.imshow(confusion_matrix, interpolation='nearest', cmap=plt.cm.Blues)  #按照像素显示出矩阵
plt.title('Normalized confusion matrix')
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes)
plt.yticks(tick_marks, classes)

thresh = confusion_matrix.max() / 2.
#iters = [[i,j] for i in range(len(classes)) for j in range((classes))]
#ij配对，遍历矩阵迭代器
iters = np.reshape([[[i,j] for j in range(classNamber)] for i in range(classNamber)],(confusion_matrix.size,2))
for i, j in iters:
    
    if(i==j):
        plt.text(j, i, format(confusion_matrix[i, j]),va='center',ha='center',c='white')  
    else:
        plt.text(j, i, format(confusion_matrix[i, j]),va='center',ha='center')   #显示对应的数字

plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.tight_layout()
plt.show()
