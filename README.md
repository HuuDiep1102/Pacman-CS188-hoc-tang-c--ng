# Pacman-CS188-hoc-tang-cuong
Câu 1 lăp lại giá trị
Viết tác nhân value iteration trong ValueIterationAgent
Lặp lại giá trị: tìm các giá trị liên tiếp (giới hạn độ sâu) (phản ánh k phần thưởng tiếp theo
Bắt đầu với V0 (s) = 0
Cho Vk,  tính giá trị độ sâu k + 1 cho tất cả các trạng thái

sử dụng 2 vòng lặp đi qua state và action để tìm ra v max từ đó tìm ra actions tiếp theo

câu2 
question2() of analysis.py
giữ nguyên discount thay đổi answerNoise =0 

Câu 3:
question3a va 3e() of analysis.py
Câu 4
QLearningAgenttrong qlearningAgents.py,
 Đối với câu hỏi này, phải thực hiện update, computeValueFromQValues, getQValue, và computeActionFromQValues.
học bằng cách thử và sai từ các tương tác với môi trường thông qua update(state, action, nextState, reward

Câu 5
Hoàn thành tác nhân Q-learning bằng cách triển khai lựa chọn hành động tham lam epsilon getAction, nghĩa là nó chọn các hành động ngẫu nhiên trong một phần thời gian epsilon và theo cách khác, giá trị Q tốt nhất hiện tại của nó. 
Câu 6
question6()trong analysis.py
Câu 7
van dung chay vs pacman
Câu 8 
ApproximateQAgentlớp qlearningAgents.py, là lớp con của PacmanQAgent.

