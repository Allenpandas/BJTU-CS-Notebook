AI模型安全威胁与鲁棒性研究

**研究内容：** AI模型安全威胁与鲁棒性研究是指对**机器学习（Machine Learning）**、**深度学习（Deep Learning）**、**强化学习（Reinforcement Learning）**等模型在应用中可能遇到的安全威胁和鲁棒性问题进行研究，旨在提高模型的安全性，使其能够在现实世界中更可靠地应用。AI模型安全威胁与鲁棒性研究内容包括但不限于以下几个方向：

- **对抗性攻击与防御：** 关注通过对输入数据进行微小修改，以欺骗模型或导致其错误预测的对抗性攻击。这些攻击可能包括**对抗性样本**、**对抗性噪声**、**对抗性样式**等。研究针对对抗性攻击的防御机制，使得模型对这些攻击更具鲁棒性。
- **鲁棒性评估：** 研究AI模型的评估方法和度量标准，以衡量模型对输入数据变化的鲁棒性。这些方法可以帮助识别模型在输入领域中的弱点，并指导鲁棒性改进的工作。
- **防御方法：** 研究人员探索开发对抗性攻击的防御方法，包括对抗性训练、输入预处理、模型修复等。这些方法旨在提高模型的鲁棒性，使其对不良输入数据具有更好的适应能力。
- **非对抗性鲁棒性：** 除了对抗性攻击外，研究人员还关注模型在面对常规噪声、数据分布变化、输入缺失等非对抗性情况下的鲁棒性。研究内容包括数据增强技术、领域适应方法、缺失数据处理等。
- **隐私和安全问题：** 研究人员关注模型在处理用户数据时可能涉及的隐私和安全问题。这包括敏感信息泄露、模型逆向工程、隐私保护技术等研究内容。
- **可解释性和可审计性：** 研究人员致力于提高机器学习模型的可解释性和可审计性，以便更好地理解模型的决策过程和预测结果。这对于安全性评估和检测潜在问题非常重要。
- **强化学习的安全性：** 强化学习模型面临的安全性挑战包括对抗性环境、误导性奖励、探索过程中的风险等。研究人员致力于开发安全的强化学习算法和方法，确保模型能够在复杂和不确定的环境中做出可靠和安全的决策。



**关键词：** Security; Software Engineering; Software Security; Security and Reliability of the Machine Learning; Security and Robustness of Machine Learning;



## 学术期刊/学术会议

**学术会议：**

- **[ASE]** International Conference on Automated Software Engineering, ASE. **（CCF-A会议）**
- **[FSE/ESEC]** ACM SIGSOFT Symposium on the Foundation of Software Engineering/ European Software Engineering Conference, FSE/ESEC. **（CCF-A会议）**
- **[SOSP]** ACM Symposium on Operating Systems Principles, SOSP. **（CCF-A会议）**
- **[ICSE]** International Conference on Software Engineering, ICSE. **（CCF-A会议）** 
- **[ISSTA]** International Symposium on Software Testing and Analysis, ISSTA. **（CCF-A会议）**

**学术期刊：**

- **[TSE]** IEEE Transactions on Software Engineering, TSE. （CCF-A期刊/IEEE Trans/中科院1区/影响因子9.322）
- **[TDSC]** IEEE Transactions on Dependable and Secure Computing, TDSC. （CCF-A期刊/IEEE Trans/中科院1区/影响因子6.791）
- **[ESE]** Empirical Software Engineering, ESE. （CCF-B期刊/中科院2区/影响因子3.762）
- **[JSA]** Journal of Systems Architecture, JSA. （CCF-B期刊/中科院2区/影响因子5.836）



## 学术团队

- 孙猛（北大·数学科学学院）：https://www.math.pku.edu.cn/teachers/sunm/pub.html
- 郑征（北航·可信智能软件研究室）：https://shi.buaa.edu.cn/zhengzheng/zh_CN/index.htm 
- 陈岑（华师大）：https://sites.google.com/site/chencenpersonalwebsite/ 
- 哥伦比亚大学·软件系统实验室 | [(Software Systems Lab, SSL)](https://systems.cs.columbia.edu/)：
  - Junfeng Yang：http://www.cs.columbia.edu/~junfeng/
  - Suman Jana：http://www.cs.columbia.edu/~suman/
  - Kexin Peng：https://sites.google.com/site/kexinpeisite/
- 阿尔伯塔机器智能研究所 | [(Alberta Machine Intelligent Institute, Amii)](https://www.amii.ca/about/our-people/)
  - Lei Ma：https://scholar.google.com/citations?user=xsfGc58AAAAJ 



## 相关文献

- **[2020-TSE]** Jie M Zhang, Mark Harman, Lei Ma, Yang Liu. Machine learning testing: Survey, landscapes and horizons.(机器学习测试:调查，景观和视野) [[pdf](https://arxiv.org/pdf/1906.10742)]

- **[2020-ICSE-Workshop] **Does Neuron Coverage Matter for Deep Reinforcement Learning?: A Preliminary Study.(神经元覆盖对深度强化学习有影响吗?:初步研究)

- **[2018-ASE]** Youcheng Sun, Min Wu, Wenjie Ruan, Xiaowei Huang, Marta Kwiatkowska, Daniel Kroening. Concolic Testing for Deep Neural Networks(深度神经网络的混合曲线测试). [[pdf](https://dl.acm.org/doi/abs/10.1145/3238147.3238172)] [[code](https://github.com/TrustAI/DeepConcolic)]

- **[2018-ASE]** Sakshi Udeshi, Pryanshu Arora, Sudipta Chattopadhyay. Automated Directed Fairness Testing.(自动定向公平性测试)

- **[2018-ICSE]** Yuchi Tian, Kexin Pei, Suman Jana, Baishakhi Ray. DeepTest: Automated Testing of Deep-Neural-Network-driven Autonomous Cars.(DeepTest:深度神经网络驱动的自动驾驶汽车自动化测试) [[pdf](https://arxiv.org/abs/1708.08559)] [[code](https://github.com/ARiSE-Lab/deepTest)]

- **[2018-ISSRE(CCF-B)]** Lei Ma, Fuyuan Zhang, Jiyuan Sun, Minhui Xue, Bo Li, Felix Juefei-Xu, Chao Xie, Li Li, Yang Liu, Jianjun Zhao, Yadong Wang. DeepMutation: Mutation Testing of Deep Learning Systems.(DeepMutation:深度学习系统的变异测试) [[pdf](https://ieeexplore.ieee.org/abstract/document/8539073/)]

- **[2018-ASE]** Lei Ma, Felix Juefei-Xu, Fuyuan Zhang, Jiyuan Sun, Minhui Xue, Bo Li, Chunyang Chen, Ting Su, Li Li, Yang Liu, Jianjun Zhao, Yadong Wang. DeepGauge: Multi-Granularity Testing Criteria for Deep Learning Systems.(DeepGauge:深度学习系统的多粒度测试准则) [[pdf](https://dl.acm.org/doi/abs/10.1145/3238147.3238202)]

- **[2018-FSE]** Jianmin Guo, Yu Jiang, Yue Zhao, Quan Chen, Jiaguang Sun. DLFuzz: Differential Fuzzing Testing of Deep Learning Systems.(DLFuzz:深度学习系统的差分模糊测试) [[pdf](https://dl.acm.org/doi/abs/10.1145/3236024.3264835)]

- **[2018-ICSE]** Jinhan Kim, Robert Feldt, Shin Yoo. Guiding Deep Learning System Testing using Surprise Adequacy(使用意外充分性指导深度学习系统测试). [[pdf](https://ieeexplore.ieee.org/abstract/document/8812069)]

- **[2018-ISSTA]** Anurag Dwarakanath, Manish Ahuja, Samarth Sikand, Raghotham M. Rao, R. P. Jagadeesh Chandra Bose, Neville Dubash, Sanjay Podder. Identifying implementation bugs in machine learning based image classifiers using metamorphic testing.(利用蜕变测试识别基于机器学习的图像分类器中的实现缺陷) 

- **[2018-ISSTA]** Yuhao Zhang, Yifan Chen, Shing-Chi Cheung, Yingfei Xiong, Lu Zhang. An empirical study on TensorFlow program bugs(TensorFlow程序bug的实证研究). [[pdf](https://dl.acm.org/doi/abs/10.1145/3213846.3213866)]

- **[2018-ICML]** Augustus Odena, Ian Goodfellow. TensorFuzz: Debugging Neural Networks with Coverage-Guided Fuzzing.(TensorFuzz:基于覆盖引导的模糊测试调试神经网络) [[pdf](https://proceedings.mlr.press/v97/odena19a.html)]

- **[2018-ASE]** Mengshi Zhang, Yuqun Zhang, Lingming Zhang, Cong Liu, Sarfraz Khurshid. DeepRoad: GAN-Based Metamorphic Testing and Input Validation Framework for Autonomous Driving Systems.(DeepRoad:基于GAN的自动驾驶系统蜕变测试和输入验证框架)

- **[2018-ATVA(CCF-C)]** Divya Gopinath, Guy Katz, Corina S. Pasareanu, Clark Barrett. DeepSafe: A Data-Driven Approach for Assessing Robustness of Neural Networks.(DeepSafe:评估神经网络鲁棒性的数据驱动方法) [[pdf](https://link.springer.com/chapter/10.1007/978-3-030-01090-4_1)]

- **[2018-FSE]** Shiqing Ma, Yingqi Liu, Wen-Chuan Lee, Xiangyu Zhang, Ananth Grama. MODE: automated neural network model debugging via state differential analysis and input selection. [[pdf](https://dl.acm.org/doi/abs/10.1145/3236024.3236082)]

- **[2017-SOSP-BestPaper]** Kexin Pei, Yinzhi Cao, Junfeng Yang, Suman Jana. DeepXplore: Automated Whitebox Testing of Deep Learning Systems.(DeepXplore：深度学习系统的自动白盒测试) [[pdf](https://arxiv.org/abs/1705.06640)] [[code](https://github.com/peikexin9/deepxplore)]

  

