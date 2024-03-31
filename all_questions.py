# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "No"
    answers["(b)"] = "No"
    answers["(c)"] = "Yes"        
    answers["(d)"] = "Yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Let us account the rule as a contradiction when we do not find any given case that jointly satisfies the rule. However, similarities and the same traits as the privileged groups were more visible than differences. An example is when a resident who followed the (2) rule did not able to (4) rule comes out as the Defaulted borrower (DB=Yes). The rules in friendships make the mosaic nature because they depend on which culture is more appealing to the individuals and they tend to follow various rules."
    answers["(b) explain"] = "Any rule that does not fit in a case is considered mutually exclusive rule and, therefore, a case (instance) cannot satisfy more than one rule. There it is overlaying another one [here]. Consequently, a Home Owner (H=Yes) could as well be a Low annual income (L=Yes) person, since such an individual will have met both conditions of a defaulted borrower (DB=yes). That is the situation when those principles may not be completely different from each other because a person can be orientated by more than one principle."
    answers["(c) explain"] = "Hence, the order of the rules is a factor in the results of classification. For instance, if a case falls under several rules, the order declares which of the rules has priority and therefore affects the act that the borrower takes at the end as the final decision response. Ranking the standards on the basis of equity, the results will be uniformly fair."
    answers["(d) explain"] = "This is due to the nature of the rule-set and the fact that the cases which do not fall within the framework of the presented rules are not covered. Students are given the task of distinguishing the cases left over. The default class is going to be an all-encompassing category making sure that cases which don't fit any of the specific rules will also be captured by this default category, too. Classlessness will be a result as some people will have their social class left unclassified. There is no place of such uncertainty model in a rule based system whose aim is to make a definite prediction."

    return answers


# -----------------------------------------------------------
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = ""
    answers["(b)"] = ""
    answers["(c)"] = ""
    answers["(d)"] = ""

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "Yes"
    answers["(b)"] = "No"
    answers["(c)"] = "No"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Rules are between pairs of cases when no case can satisfy more than one rules at a time.In this set:R1 defines birds as air-breathing organisms devoid of giving birth. R2: In this example, fish takes the place of any aquatic vertebrate that is oviparous or lays eggs. R3: Warm-blooded animals are the mammals. R4 provides the definition of the reptiles as the animals have live birth but are not birds and also not fishes. These rules"
    answers["(b) example"] = "The rules set will be so massive that it shall combine all of the possible cases. The rules will be determined based on the incoming data and at least one of the rules will classify all of it. As well as that, the regulations would apply only in some selected cases. Consequently, amphibians and birds are not pointed out at all, because neither of these rules mentions warm-blooded, cold-blooded or the vertebrates who filled eggs and do not fly such as penguins and salamanders."
    answers["(c) example"] = "On account of the absence of connection most of them are suitable somewhat in one condition and of unity of the act could not determine the sequence of their application. Lack of randomness will be experienced because it will not be dependent on the order of the examples. The Step is no different from the other but the crispness may differ from time to time. Although this may be so but it should but pointed that if there are any conditions or reasons which are not within this list would not show up in the rules category and this is a different issue from matching reasons to the rules."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The gradient at the (k+1)th layer is used to calculate the value of the gradient at the kth layer, by applying the chain rule again to get the correct value, which is the base to update the weights in every layer of the network"
    answers["(b) explain"] = "When an NN process is making the transition from kth to k+1th level, activation at k+1 is derived by multiplying the weights of the nodes at k and summing them together; then, an activation function is applied."
    answers["(c) explain"] = "The vanishing gradient problem accrues when propagating gradients through intermediate layers becomes tedious and mostly insignificant gradients tend to occur hence no or minimal learning at the earlier layers thus, this exposes the issue of disappearing backpropagating training errors."
    answers["(d) explain"] = "Even if ANN performance is 100%, having gradients of the loss function at each layer equal to zero doesn't imply it too. If it's the model a global optimum, then the gradient vector is equal to zero. Particularly, there will be no perfect follow-up of the training set but models that match the data due to the fact that the loss function can allow for margins of error, which will have non-zero gradients."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.28
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "No"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.4
    answers["(c) P(X_2=1 | +)"] = 0.4
    answers["(c) P(X_2=1 | -)"] = 0.5
    answers["(c) P(X_3=1 | +)"] = 0.16
    answers["(c) P(X_3=1 | -)"] = 0

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "The figure KNN (a) illustrates that there are disjunctive colored clusters, i.g. without class overlap. That aspect is obvious in case of this situation because K value with a small algebraic value is mostly preferred due to the fact that the instances of each class are densely contained in the given space. Ok, it is worth mentioning that at this point K = 1 actually gives an edge, but this error is not very probable mainly because not too many neighbors are involved. With K=50 because the splitting of different classes is better than the first scenario, it could be the case that K=50 is too much, which could over smooth the decision boundary so the second option would be better in this case."
    answers["(b) explain"] = "Figure KNN Plot (b) concentrated at the places where there was more space between classes, meaning that each data points belonging to two classes is not necessarily representative of the distribution of overall class as it is affected by noise or class overlapping. In this instance, instead of a small K we would like a won big peer group. The decision is made from a more comprehensive data set, which is also kind to noise. An ideal compromise could be K = 5. It might prevent decision boundaries, which are too sensitive to outlier, like they are in K = 1 and yet it also has enough detail to respond to the complexities of real class borders instead of being too smooth and underfit in case of K = 50. At the same time, when the decision boundary is unclear and different data points give rise to such condition. The K = 50 algorithm may have difficulty at capturing some of the details in the data."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.4
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.4
    answers["(a) P(A=1|-)"] = 0.8
    answers["(a) P(B=1|-)"] = 0.0
    answers["(a) P(C=1|-)"] = 0.4

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "1. Count the number of positive (+) occurrences that related to a class by the attribute; then count down by the number of positive (+) occurrences. From step 1, divide counts by counts from step 2 to get \( P(Attribute = 1 | Class = +) \). Now, do the same for negative class (-).Count the instances where A=1 and the class is +**: Those are shown through the table; where cases numbers 5 and 10 have A=1 and have the classification of positive. Find the total number of positive instances: Examples 2, 5, 6, 9, and 10 are positive, thus we have 5 positive cases. Calculate; \( P(A=1 | +) \)(of which there were 2 \( A=1 )."

    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.064
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "Given a classiﬁer of a Naive Bayes test that has all the features set to 1, the classiﬁer assigns it to the positive class. Hence, from the condition on the other feature in regard to the negative class has a value of exactly zero that results in a zero value of the joint likelihood of the negative class. Therefore, caught in the middle of les s'il y a deux classes, the only thing that works is the positive class as a predictor."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.3
    answers["(c) P(A=1,B=1)"] = 0.1

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "No"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.7
    answers["(d) P(A=1,B=0)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = None
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = None
    answers["(e) P(A=1|+)"] = None
    answers["(e) P(B=1|+)"] = None

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = None

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  None
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
