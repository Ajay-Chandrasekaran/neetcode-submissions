impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let (a, b) = (s1.as_bytes(), s2.as_bytes());
        let n = a.len();
        if n > b.len() {
            return false;
        }

        let idx = |c: u8| (c - b'a') as usize;

        // diff[c] = count in s1 - count in current window of s2
        let mut diff = [0i32; 26];
        for (&x, &y) in a.iter().zip(b) {
            diff[idx(x)] += 1;
            diff[idx(y)] -= 1;
        }

        for (&incoming, &outgoing) in b[n..].iter().zip(b) {
            if diff == [0; 26] {
                return true;
            }
            diff[idx(incoming)] -= 1;
            diff[idx(outgoing)] += 1;
        }

        diff == [0; 26]
    }
}