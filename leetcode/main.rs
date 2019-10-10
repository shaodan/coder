struct Solution {
}

impl Solution {
    // solution here
    pub fn my_sqrt(x: i32) -> i32 {
        // Solution-1 Newton
        // newton(x)

        // Solution-2 Binary Search
        binary_search(x)
    }
}

fn newton(x: i32) -> i32 {
    let longx = x as i64;
    let mut r = longx;
    while r*r > longx {
        r = (r + longx/r) / 2;
    }
    r as i32
}

fn binary_search(x: i32) -> i32 {
    if x == 0 {
        return 0;
    }
    let mut left = 1;
    let mut right = x;
    let mut mid;
    let mut quo;

    while left < right-1 {
        mid = (left + right) / 2;
        quo = x / mid;
        if quo == mid {
            return mid;
        }
        if mid > quo  {
            right = mid;
        } else {
            left = mid;
        }
    }
    left
}

fn main() {
    println!("Hello Leetcode!");
    for i in 0..10 {
        println!("{} {}", i, Solution::my_sqrt(i));
    }
}
