# 1.Manga FaceNet
   The purpose of the project is used to identify face in manga pages, so that it will be helpful to search the particular character by recognizing manga face
    This code is just implementation of [Manga FaceNet](https://www.cs.ccu.edu.tw/~wtchu/papers/2017ICMR-chu2.pdf)
    
 ## Architecture
 * Apply selective search algorithm to manga pages and then
 * Feeding that candidate regions to Manga FaceNet(CNN)
 * Result will be predicted as Face or Not

## Accuracy and Loss of Manga FaceNet
  
 "Epoch 111/111\n",
            "500/500 [==============================] - 204s 409ms/step - loss: 0.0078 - accuracy: 0.9974 - val_loss: 0.0012 - val_accuracy: 0.9964\n"

1. This FaceNet model is trained with 13999 images of face region and 10000 images of not face region, validated with 3000 of face and not face region
