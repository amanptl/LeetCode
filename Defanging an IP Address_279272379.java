class Solution {
    public String defangIPaddr(String address) {
        String answer;
        answer = address.replace(".", "[.]");
        return answer;
    }
}
