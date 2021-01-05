# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    # Voi noise = 0 van de tro len sang to va tac nhan se luon ket thuc
    # o trang thai du kien, nen chinh sach toi uu se vuot qua cau
    #vi no se luon di chuyen theo huong toi da hoa phan thuong mong doi
    answerNoise = 0
    return answerDiscount, answerNoise

def question3a():
    # vi muon nhanh chong di chuyen den loi thoat phan thuong va do on doi
    # duoc giu lai de co gang thoat ra cang som cang tot
    answerDiscount = 1
    answerNoise = 0.2
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # Neu khong kha thi, tra ve  'NOT POSSIBLE'

def question3b():

    answerDiscount = 0.3
    answerNoise = 0.3
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward


def question3c():

    answerDiscount = 1
    answerNoise = 0.2
    answerLivingReward = -0.5
    return answerDiscount, answerNoise, answerLivingReward


def question3d():
    
    answerDiscount = 1
    answerNoise = 0.2
    answerLivingReward = -0.03
    return answerDiscount, answerNoise, answerLivingReward


def question3e():

    answerDiscount = 1
    answerNoise = 0.2
    answerLivingReward = 1000
    return answerDiscount, answerNoise, answerLivingReward


def question6():
    answerEpsilon = 0.1
    answerLearningRate = 0.8
    # not possible because to find optimal path 99%, 50 episode is too small
    # it needs more episode to clearly explore
    return 'NOT POSSIBLE'
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
