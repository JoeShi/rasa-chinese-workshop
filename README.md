# RASA 构建中文 Chatbot 

这个 tutorial 将通过动手实验的方式学习 NLP 和 Chatbot 相关的知识。我们将从 NLP 的一些基本概念入手，同时我们会使用 [RASA](https://rasa.com/) 来构建中文 Chatbot。

这是一个计划长期维护的项目，将在这个项目中不断完善关于 NLP 及 chatbot 的内容，欢迎共同探讨。有任何问题，欢迎通过 [GitHub Issues](https://github.com/JoeShi/rasa-chinese-workshop/issues)进行探讨。

## 内容

本 tutorial 的每一个章节都是一个 Jupyter notebook, 方便大家直接运行。在开始实验之前，请先完成[准备工作](#准备工作)。建议通过 git clone 到本地，通过 Jupyter notebook 的方式阅读。

- [x] [NLP (自然语言处理) 中的常用知识点](nlp_basics.ipynb)

- [x] [中文分词技术](nlp_tokenization.ipynb)

- [ ] 中文词性标注与命名实体识别

- [ ] 句法分析和情感分析

- [ ] 文本向量化

- [x] [RASA 项目简介](rasa_introduction.ipynb)

- [x] [RASA 项目中的数据准备阶段](rasa_prepare_data.ipynb)

- [x] [RASA NLU Training 实战](rasa_nlu_training.ipynb)

- [x] [RASA 构建天气查询机器人实战](rasa_core_weather_bot.ipynb)

- [x] [RASA Chatbot 在 Kubernetes 中的部署实战](rasa_k8s_chatbot.ipynb)

- [ ] RSSA X 在 Kubernetes 中的部署实战

## 准备工作

本教程需要安装 [Anaconda](https://www.anaconda.com/), 如果在国内安装很会慢，建议使用
[清华的Anaconda安装包 Mirror](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/).

### 将 Anaconda 的源修改为清华大学

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 创建 conda env

```shell script
conda create --name rasa python=3.6.8
conda activate rasa
pip install -r requirements.txt

# ONLY for development
pip install nest_asyncio
pip install jupyterlab
```

### 下载语料库

[这篇文章](http://www.crownpku.com/2017/07/27/%E7%94%A8Rasa_NLU%E6%9E%84%E5%BB%BA%E8%87%AA%E5%B7%B1%E7%9A%84%E4%B8%AD%E6%96%87NLU%E7%B3%BB%E7%BB%9F.html)用中文wikipedia和百度百科语料生成了一个total_word_feature_extractor_chi.dat，分享如下：

```
链接：https://pan.baidu.com/s/1kNENvlHLYWZIddmtWJ7Pdg 密码：p4vx
```

请先下载并放置到 `data/` 目录下，我们在后续的 tutorial 中解释语料库。

## 学习资料/参考资料

[Chatbot 产品经理指北](http://www.sohu.com/a/345594550_114819)

### NLP 相关 Libs
[snownlp:Simplified Chinese Text Processing](https://github.com/isnowfy/snownlp)


### NLP 学习资料
[Python 自然语言处理实战-核心技术与算法](https://item.jd.com/12375644.html)

### RASA 参考资料
[Chinese bot](https://forum.rasa.com/t/chinese-bot/12416)
[用Rasa_NLU构建自己的中文NLU系统](http://www.crownpku.com/2017/07/27/用Rasa_NLU构建自己的中文NLU系统.html)
[RASA UI](https://github.com/paschmann/rasa-ui)
[Articulate](https://github.com/samtecspg/articulate)