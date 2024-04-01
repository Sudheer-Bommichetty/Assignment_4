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
    answers["(a) explain"] = "When multiple rules are not satisfied by a single case, it is considered a conflicting rule. Regretfully, there is a chance that there will be overlaps in this pool. A homeowner who meets rule (1) in this instance may also have a degraded annual income under rule (3) and be designated as the defaulted borrower (DB = Yes). However, because a person's unique qualities may stimulate several rules, this fact does not render the rules mutually inconclusive." 
    answers["(b) explain"] = "A case (instance) cannot satisfy more than one rule in a mutually exclusive rule scenario, which is any rule that does not apply in that particular context. It overlaps with another one here. Consequently, a person with a low annual income (L= Yes) may also be a home owner (H= Yes), meeting both requirements that a defaulted borrower (DB = yes) ought to have. Since multiple rules might direct an individual's actions, they might not be mutually exclusive in this situation."
    answers["(c) explain"] = "The sequence of the rules may therefore affect the final categorization outcome because they are not independent. When a situation is subject to many rules, the order determines which rule applies first, affecting the default borrower's ultimate reaction. Ranking the rules guarantees consistently equitable outcomes."
    answers["(d) explain"] = "If one excludes instances when the rules as provided are not followed, the rule set is incomplete. Unmatched cases must be classified using the classes. The catch-all default class will ensure that all cases, including those that don't fit under any particular set of rules, are covered by this categorization. Some of the people will continue to be unclassified if there is no default class. In a rule-based system where the ultimate goal is to generate precise forecasts, that is undesirable."

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
    answers["(a) example"] = "When no case can meet more than one rule at once, rules are between pairs of cases.Within this set, R1 will delineate species that breathe air but do not reproduce like birds.According to this concept, a fish is any aquatic animal that is not oviparous.R3: A mammal is characterized as any warm-blooded vertebrate.R4 classifies animals that give birth alive as reptiles, not fish or birds.Since each rule requires a unique combination of attribute values to be activated that are not shared by other rules, these rules are mutually exclusive."
    answers["(b) example"] = "The ruleset will be so large as to encompass any scenario conceivable. Every entry in the data collection will be evaluated, and at least one rule will categorize every one of them. Furthermore, these guidelines do apply in certain circumstances. Because none of these criteria cover vertebrates that are warm-blooded and give birth but are not airborne (like penguins) or cold-blooded and give birth (like salamanders), amphibians and birds are not particularly referenced by these laws."
    answers["(c) example"] = "Because they are fragmented, only one example would be relevant in a particular situation, hence the sequence in which they are used is irrelevant. There won't be any chance in the classification process because every example, in any order, will be classified in the same way—that is, as a reflection of one of the rules being followed. However, it should be noted that some reasons that are not on the list may not even be labeled, which is a separate matter entirely from reasons that fall under the purview of the guidelines."

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
    answers["(a) explain"] = "The gradient at the (k+1)th layer serves as the foundation for updating the weights of each layer in the network. The gradient at the kth layer is computed using the chain rule to obtain an accurate value."
    answers["(b) explain"] = "The activation at k+1 is computed using the weights of the nodes at k and activated through a summation and function application when an ANN process moves from the kth layer to the k+1th."
    answers["(c) explain"] = "The vanishing gradient problem in ANN training occurs when the algorithm finds it difficult to propagate gradients through backward layers, leading to little or no learning at the earlier layers. This problem is unrelated to backpropagating training errors that cause disappearance."
    answers["(d) explain"] = "This does not imply that gradients of the loss function with respect to weights at each layer will equal zero, even in the case of perfect ANN performance. The gradient will be zero if the model is to be at a global optimal minimum. However, as loss functions frequently allow for error margins, a model customized for the particular data can still produce a perfect classification of the training set and have non-zero gradients."

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
    answers["(a) explain"] = "Plotting in figure KNN (a) indicates that there is no class overlap because the clusters are easily distinguished by their various colors. Since all of the instances of each class are densely packed together in the available space, K, which has a small value, is considered the best option in this type of situation. Since there aren't many neighbors involved at this point, where K = 1 offers somewhat superior performance, this kind of error in judgment is actually quite unusual. Class separation is preferable to scenario A, however K=50 might be excessive in this instance and oversmooth the decision boundary, thus the second option would be preferable."
    answers["(b) explain"] = "Due to noise and class overlapping, each occurrence of a class is not always indicative of the general class distribution, as shown by Figure KNN (b), which displayed the greater overlapping space between the classes. Since the classifier's conclusion is based on a larger range of neighbors, a huge k would be better in this case since it eliminates the sound effect of noise. A suitable balance would be K = 5, which is detailed enough to adjust to the complexity of genuine class boundaries better than K = 50, which might be too smooth and lead to the model underfitting, but avoids a smoother decision boundary from being overly sensitive to outliers, as it is for K = 1. In contrast, in the former scenario, when the decision boundary is unclear, the K"
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
    answers["(a) P(A=1|+) explain your answer"] = "Determine how often an event occurs when the attribute is 1 and the class is positive (+).Reduce the count by the quantity of positive (++) events. P(Attribute = 1 | Class = +) \) is obtained by dividing the counts from step 1 by the counts from step 2.4. Proceed similarly with the negative class (-).Determine how many times A=1 and the class is +**. These are shown in the table, where examples 5 and 10 are categorized as positive and have an A=1 value.Add up all of the favorable examples: Five affirmative situations can be found because examples 2, 5, 6, 9, and 10 are all positive.Determine \( P(A=1 | +) \)**: Out of the 5 favorable instances, there were 2 \( A=1 \); hence, \( P(A=1 |+) = \frac{2}{5} \)."

    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.064
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "The classifier places the data in the positive class for a Naive Bayes test case when all characteristics are set to 1. Consequently, the joint likelihood of the negative class would be exactly zero since the conditional probability for one characteristic given the negative class would also be zero. Thus, the only plausible prediction that can be made is the positive class."
  
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
    answers["(d) A independent of B?"] = "No"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.4
    answers["(e) P(A=1|+)"] = 0.8
    answers["(e) P(B=1|+)"] = 0.5

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "Yes"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "In essence, given the class+ provided, a, and b are independent. In the framework of conditional independence constraints, this primarily addresses the requirement for independence of conditionality within the time NO conditionality constraints exist in the Naïve Bayes classifier for A and B to be considered independent under the final class if P(A&B/class)=P(A/class) * P(B/class)."
  
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
