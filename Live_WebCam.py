#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install opencv-python


# In[17]:


import cv2


# In[18]:


cap = cv2.VideoCapture(0)


# In[19]:


while True:
    ret, frame = cap.read()
    IMG_GRAY = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam', IMG_GRAY)
    if cv2.waitKey(1) & 0xFF == ord('x'):  # Corrected waitKey condition
        break

cap.release()  # Release the VideoCapture object
cv2.destroyAllWindows()


# In[26]:


#Live Recording
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret, frame=cap.read()
    out.write(frame)
    img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('webcam',img_gray)
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()


# In[25]:


cv2.destroyAllWindows()


# In[ ]:




