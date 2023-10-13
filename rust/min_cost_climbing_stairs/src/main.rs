
fn main(){
    //let solution_instance = Solution{cost: vec![1,2]};
    //https://leetcode.com/problems/min-cost-climbing-stairs/?envType=daily-question&envId=2023-10-13
    Solution::hello_world();
    Solution::min_cost_climbing_stairs(vec![1,2,2,0]);
}


struct Solution{

}
impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        //constraints
        //2 <= cost <= 1000
        //0 <= ost[i] <= 999

        //purchasing a step means you can climb 1 or 2 steps
        //e.g. 1,2,3 -> u can go to 2 or 3 depending on which step is cheaper

        let mut total_cost: i32 = 0;
        let cost_len = cost.len() - 1; //-1
        let start: usize;
        if cost_len == 2{
            if cost[0] + cost[2] < cost[1] {
                total_cost = cost[0] + cost[2];
            } else {
                total_cost = cost[1];
                };
            println!("Total1 (broke early) cost: {}",total_cost);
            return total_cost;
        } else if cost_len == 3{
            total_cost = if cost[0] + cost[2] > cost[1] + cost[cost_len] {cost[1] + cost[cost_len]} else {cost[0] + cost[2]};
            total_cost = if total_cost > cost[1] + cost[2] {cost[1] + cost[2]} else {total_cost};
            println!("Total2 (broke early) cost: {}",total_cost);
            return total_cost;
        } else{
            start = if cost[0] >= cost[1] {1} else {0}
        }
        
        total_cost += cost[start];
        
        let mut index = start;

        while index <= cost_len{
            println!("{}",index);
            index += 1;
            println!("!!Index: {}\nClen: {} ",index,cost_len);
            if index >= cost_len{
                break;
            } else{
                //if its 3rd last
                //e.g. [...0,1,2,2] -> need to choose 0 - 2 instead of 0-1-2 (since first arg will choose (1,2) -> 1)
                if index == cost_len-2{
                    index = if cost[index-1] + cost[index] + cost[cost_len] > cost[index-1] + cost[index+1] {index+1} else {index}
                } else{
                    index = if cost[index] >= cost[index + 1] {index+1} else {index};
                }
            }
            println!("Selected Index: {}\nValue: {}", index, cost[index]);
            total_cost += cost[index];
        }

        println!("Total Cost: {}", total_cost);
        return total_cost;
    }
    
    pub fn hello_world(){
        println!("Hello, World from Solution!");
    }
}