class Node {
    public:
        int val;
        Node* next;
        Node(int v) {
            val = v;
            next = NULL;
        }

        Node(int v, Node* n) {
            val = v;
            next = n;
        }
};

class LinkedList {
private:
    Node* head;
    Node* tail;

public:
    LinkedList() {
        head = new Node(-1);
        tail = head;
    }

    int get(int index) {
        int pos = 0;
        Node* curr = head -> next;

        while (curr != NULL) {
            if (pos == index) {
                return curr -> val;
            }
            pos++;
            curr = curr -> next;
        }
        return -1;
        
    }

    void insertHead(int val) {

        Node* newHead = new Node(val);
        newHead -> next = head -> next;
        head -> next = newHead;

        if (newHead -> next == NULL) {
            tail = newHead;
        }

    }
    
    void insertTail(int val) {
        Node* newTail = new Node(val);
        tail -> next = newTail;
        tail = newTail;
        return;
    }

    bool remove(int index) {
        int pos = 0;
        Node* curr = head;

        while (pos < index && curr != NULL) {
            pos++;
            curr = curr -> next;
        }

        if (curr != NULL && curr -> next != NULL) {
            if (curr -> next == tail) {
                tail = curr;
            }
            Node* toDel = curr -> next;
            curr -> next = curr -> next -> next;
            delete toDel;
            return true;
        }        
        return false;
        
    }

    vector<int> getValues() {

        vector<int> res;
        Node* curr = head -> next;
        while (curr != NULL) {
            res.push_back(curr -> val);
            curr = curr -> next;
        }
        return res;
        
    }
};
