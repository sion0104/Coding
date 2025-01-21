import Foundation

func solution(_ numLog:[Int]) -> String {
    var answer = ""
    
    for i in 0..<(numLog.count - 1){
        let difference = numLog[i+1] - numLog[i]
        
        switch difference {
        case 1:
            answer += "w"
        case -1:
            answer += "s"
        case 10:
            answer += "d"
        case -10:
            answer += "a"
        default:
            break
        }
    }
    
    return answer
}