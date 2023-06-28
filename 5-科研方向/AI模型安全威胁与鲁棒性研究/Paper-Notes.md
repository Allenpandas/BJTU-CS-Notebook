## 2022

- **[arkiv-2022]** Amirhossein Zolfagharian, Manel Abdellatif, Lionel Briand, Mojtaba Bagherzadeh, Ramesh S. **Search-Based Testing Approach for Deep Reinforcement Learning Agents.** [[pdf](https://arxiv.org/abs/2206.07813)] [[code](https://github.com/amirhosseinzlf/STARLA)]
  - **摘要：**
    - 在过去的十年，深度强化学习算法被越来越多地用于解决各种决策问题（various decision-making problems），例如自动驾驶和机器人。然而，当部署在安全关键环境（safety-critical environments）重时，这些算法面临着巨大的挑战，因为（since）它们经常表现出导致潜在严重错误（potentially critical errors）的不正确行为（erroneous behaviors）。评估深度强化学习智能体安全的一种方法是对他们进行测试，目的是检测在执行期间（during their execution）可能导致致命故障（critical failures）的缺陷（faults）。这就提出了一个问题（this raises the question of …），即：我们如何有效的测试DRL策略，以确保他们的正确性和符合安全需求（adherence to safety requirements）。现有的大多数DRL测试工作使用的是对抗攻击（adversarial attacks）方法来扰动智能体的状态或者动作。然而，这些攻击经常导致环境出现不现实的状态。他们的主要目标是测试DRL智能体的鲁棒性（robustness），而不是测试智能体策略是否符合需求。由于DRL环境的巨大状态空间、测试执行的高成本、以及DRL算法黑盒性质（black-box nature），对DRL智能体进行详尽的测试（exhaustive testing）是不可能的。
    - 在本文中，我们提出了一个基于搜索的强化学习智能体测试方法（Search-based Testing Approach of Reinforcement Learning Agents, STARLA）来测试测试DRL智能体的策略，通过在有限的测试预算内（a limited testing budget）来有效的搜索智能体的执行失败。我们使用机器学习模型和专用的遗传算法（a dedicated genetic algorithm）将搜索缩小至错误的episodes。我们将STARLA应用到被广泛作为基准的深度Q-learning算法的智能体上，发现它能够检测更多的与智能体策略相关的缺陷，明显优于（significantly outperforms）随机测试（Random Testing）。我们还研究了基于我们的搜索结果，如何提取描述DRL智能体缺陷episodes的规则，这些规则可以被用来理解智能体失败的条件，从而评估部署风险（assess its deployment risks）。

---

- **[IJCAI-2022]** Martin Tappler, Filip Cano Córdoba, Bernhard K. Aichernig, Bettina Könighofer. **Search-Based Testing of Reinforcement Learning.** [[pdf](https://arxiv.org/abs/2205.04887)]

  - **摘要：**
    深度强化学习的评估本质上具有挑战性。特别是学习策略的不透明性（opaqueness of learned policies）以及智能体和环境的随机性质（stochastic nature），导致了深度强化学习智能体的行为测试变得困难。我们提出了一个基于搜索的测试框架，可以实现广泛的新颖分析功能（analysis capabilities），用于评估DRL智能体的安全和性能。对于安全测试，我们使用了一个搜索算法（a search algorithm）来搜索解决RL任务的参考根据（reference trace）。搜索的回溯状态（backtracking states），称为边界状态（boundary states），构成安全临界状况（safety-critical situations）。我们创建了安全测试套件（safety test-suites），用于评估RL智能体在这些边界状态附近逃脱（escapes）安全临界情况。对于鲁棒性的性能测试，我们通过模糊测试（fuzz testing）创建了一组不同的跟踪。这些模糊轨迹用于将智能体带入各种可能未知的状态，从中将智能体的平均性能与模糊轨迹的平均性能进行比较，我们将基于搜索的测试方法应用于任天堂的超级马里奥兄弟的RL。

## 2021

- **[NeurIPS-2021]** Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron C. Courville, Marc Bellemare. **Deep Reinforcement Learning at the Edge of the Statistical Precipice.** [[pdf](https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html)] [[code](https://github.com/google-research/rliable)] （CCF-A会议/NeurIPS-2021杰出论文奖）

  - **摘要：**

    Deep reinforcement learning (RL) algorithms are predominantly evaluated by comparing their relative performance on a large suite of tasks. 深度强化学习算法主要（predominantly）通过比较它们在大量任务（a large suite of tasks）中的相对性能（relative performance）来评估。大多数已发表的深度RL基准测试结果比较了总体表现（aggregate performance）的点估计值（point etimates），例如任务重的平均值和中值，却忽略了使用有限次训练时所隐含的统计的不确定性（statistical uncertainty implied ）。从街机学习环境（ALE）开始，向计算要求高的基准的转变导致了对每个任务只评估少量运行的做法，加剧了点估计值的统计不确定性。

    ……（待更新）



## 2018

- **[ICSE-2018]** DeepTest: automated testing of deepneural-network-driven autonomous cars



- [ASE-2018] DeepGauge: multi-granularity testing criteria for deep learning systems. [[pdf](https://dl.acm.org/doi/abs/10.1145/3238147.3238202)] [[code](https://deepgauge.github.io/)]

  - **摘要：**

    Deep learning (DL) defines a new data-driven programming paradigm that constructs the internal system logic of a crafted neuron network through a set of training data. 

    深度学习定义了一种新的数据驱动的编程范式（programming paradigm），通过一组训练数据，构建精心制作的神经元网络的内部系统逻辑。

    We have seen wide adoption of DL in many safety-critical scenarios. 

    我们已经看到DL被广泛应用到了许多安全关键场景中。

    However, a plethora of studies have shown that the state-of-the-art DL systems suffer from various vulnerabilities which can lead to severe consequences when applied to real-world applications. 

    

    Currently, the testing adequacy of a DL system is usually measured by the accuracy of test data. Considering the limitation of accessible high quality test data, good accuracy performance on test data can hardly provide confidence to the testing adequacy and generality of DL systems. Unlike traditional software systems that have clear and controllable logic and functionality, the lack of interpretability in a DL system makes system analysis and defect detection difficult, which could potentially hinder its real-world deployment. In this paper, we propose DeepGauge, a set of multi-granularity testing criteria for DL systems, which aims at rendering a multi-faceted portrayal of the testbed. The in-depth evaluation of our proposed testing criteria is demonstrated on two well-known datasets, five DL systems, and with four state-of-the-art adversarial attack techniques against DL. The potential usefulness of DeepGauge sheds light on the construction of more generic and robust DL systems.

## 2017

- **[SOSP-2017]** Kexin Pei, Yinzhi Cao, Junfeng Yang, Suman Jana. **DeepXplore: Automated Whitebox Testing of Deep Learning Systems.** [[pdf](https://arxiv.org/abs/1705.06640)] [[code](https://github.com/peikexin9/deepxplore)] （CCF-A会议/SOSP-2017最佳论文）
  - **关键词：**
    whitebox testing; differential testing（差分测试）; Deep learning testing; neuron coverage（神经元覆盖率）; corner case（边角案例/极端案例，不常见且在规定范围内的案例）
  - **贡献：**

    - 作者引入神经元覆盖率（neuron coverage）作为深度学习系统第一个白盒测试指标；
    - 作者证明，最大化神经元覆盖率（maximizing neuron coverage）的同时，在相似的深度学习系统中找到大量的行为差异（behavioral differences）可以表述为一个联合优化问题（a joint optimization problem）；作者提出了一个基于梯度的方法（gradient-based algorithm）解决了该问题；
    - DeepXplore作为第一个白盒DL测试框架（the first whitebox DL-testing framework），在15个最先进的DL模型（15 state-of-the-art DL models）中暴露了数千个极端案例（corner case behaviors）；
    - 作者表明，基于DeepXplore生成的测试样例（the tests generated by DeepXplore）可以用于重新训练相应的DL系统，可以提高3%的分类准确度。
  - **结论：**
    - 作者设计并实现了DeepXplore（这是第一个用于系统测试DL系统的白盒测试框架）；
    - 作者引入了一个新的度量——神经元覆盖率（neuron coverage），用于测试DNN中有多少规则被一组输入执行；
    - DeepXplore利用梯度上升法解决了一个联合优化问题，可以最大限度的提高神经元覆盖率，发现潜在的错误行为。
    - DeepXplore可以在基于5个真实的数据集上训练的15个DNN模型中发现数千个错误行为。















q
