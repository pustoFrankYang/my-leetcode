class FileSystem {
    struct TrieNode {
        int value;
        unordered_map<string, TrieNode*> children;
        TrieNode(int v) : value(v), children(unordered_map<string, TrieNode*>()) {}
    };
    TrieNode* root;
public:
    FileSystem() {
        root = new TrieNode(0);
    }
    
    bool createPath(string path, int value) {
        stringstream ss(path);
        string item;
        TrieNode* curr = root;
        bool prevNotFound = false;
        while (getline(ss, item, '/')) {
            if (item == "") continue;
            if (prevNotFound) return false;
            if (curr->children.find(item) == curr->children.end()) { // not found
                prevNotFound = true;   
            } else {
                curr = curr->children[item];
            }
        }
        if (prevNotFound) {
            curr->children[item] = new TrieNode(value);
            return true;
        } else {
            return false;
        }
    }
    
    int get(string path) {
        stringstream ss(path);
        string item;
        TrieNode* curr = root;
        while (getline(ss, item, '/')) {
            if (item == "") continue;
            if (curr->children.find(item) == curr->children.end()) { // not found
                return -1;   
            } else {
                curr = curr->children[item];
            }
        }
        return curr->value;
    }
};

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem* obj = new FileSystem();
 * bool param_1 = obj->createPath(path,value);
 * int param_2 = obj->get(path);
 */