# 🐳 Whale_Fin_Image_Classification_Project #
----------------------------
+ 이 프로젝트는 전북대 창의적 IT 공학설계의 결과물이다. 
### Reasons for Project Planning ###
> Have you ever seen a whale up close? It's quite rare to see whales in South Korea, even in the vast blue Pacific Ocean. Even if you're lucky enough to see a whale, there's a high chance that you'll only see its fin above the water. Despite this, it's an incredible experience, and you may be curious to know which species of whale it is. It's usually difficult for the average person to distinguish between different whale species just by seeing their fins. But don't worry, our model can help you quickly and accurately identify which species of whale it is!
-------------------------------
### Model Introduction ##
> Our embedded model on the web is a Convolutional Neural Network (CNN) based on VGGNet (vgg11), which has been trained with approximately 21,000 images for 140 epochs. With this trained model, we can identify the species of 15 different whales. Unfortunately, other marine mammals such as dolphins and sharks are not included in the classification targets of our model, and the supported whale species are shown in the left image. Please feel free to input your own image to check the whale species!

+ Classification Targets: 

    Blue Whale | Fin Whale | Humpback Whale | Sperm Whale | Beluga Whale
    ---- | ---- | ---- | ---- | ----
    Minke Whale | Sei Whale | Bryde's Whale | Mink Whale | Dall's Porpoise
    Common Porpoise | False Killer Whale | Killer Whale | Risso's Dolphin | Southern Right Whale
-------------------------------
### Source File ###
<div>
    <a href="https://colab.research.google.com/drive/1J0MWPolMQmzzW8IPybP0Zk8WjykTF_Vy?usp=sharing">
    <img src="https://img.shields.io/badge/Go To Colab-F9AB00?style=flat-square&logo=google colab&logoColor=white"/></a>
    <a href="https://drive.google.com/file/d/1F4eLUG1We_V08n4l8JvAbw8b5MC8HBai/view?usp=sharing">
    <img src="https://img.shields.io/badge/Download Model-4285F4?style=flat-square&logo=Google Drive&logoColor=white"/></a>
</div>

-------------------------------
### 모델 사용법 ###
+ 웹 서버 구동 파일 이름 : server.py
    + 서버를 구동할 경우
        > 파일 경로를 설정한후 다음과 같이 입력
        <pre><code>
        python app.py
        </code></pre>
-------------------------------

![KakaoTalk_20220811_230845463](https://user-images.githubusercontent.com/79682941/184157292-bc23e744-b01c-46ff-98c8-942f39729972.png)

![KakaoTalk_20220811_230929582](https://user-images.githubusercontent.com/79682941/184157295-5773aa36-3174-4fbc-8ee8-a7ab0e87877a.png)

이 프로젝트는 Eoryeong_Goh, Chaeu_Park, Seungheon_Ok, Seungchan_Lee에 의해 만들어짐 

