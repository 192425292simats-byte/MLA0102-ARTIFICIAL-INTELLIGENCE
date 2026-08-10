from sklearn.tree import DecisionTreeClassifier

X = [[25,50000],[35,70000],[22,30000],[45,90000]]
y = [0,1,0,1]

model = DecisionTreeClassifier()
model.fit(X,y)

age = int(input("Enter Age: "))
income = int(input("Enter Income: "))

result = model.predict([[age,income]])

if result[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")
