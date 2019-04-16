```cpp
#include <iostream>
//template<typename T>
//estrutura de uma arvore por struct

class Binarytree{
    private:
        struct Node
        {
            int info; // o int pode ser trocado para outros tipos
            Node *left, *right;
        };
        
        Node *root;

    //deletando por root
    void delete_by_merging(Node** n){
        auto node = *n;

        if(node == nullptr) return;

        if (node->right == nullptr) //caso 1 e 2
            *n = node->left;
        else if (node->left == nullptr)
            *n = node->right; //caso 2
        else{
            auto temp = node->left;

            while(temp->right)
                temp = temp->right;
            
            temp->right = node->right;
            *n = node->left;
        }
        delete node;
    }
    //pesquisando tamanho
    int size(const Node *node)const{
        return node ? size(node->left) + size(node->right) +1 : 0;
    }

    //algoritmo de busca
    bool search(Node *node, int info) const{
        while(node){
            if(info == node->info)
                return true;
            else if(info<node->info)
                node = node->left;
            else
                node = node->right;            
        }
        return false;
    }

    public:
        Binarytree() : root(0) {} //substituir 0 por nullptr

        //inserindo elementos na arvore
        void insert(int info){
            Node * node = root, //começa no root
            *prev = 0;

            //busca o ultimo nó e coloca em prev enquanto houver nó.
            while(node){
                prev = node;
                if(node->info == info)
                    return;
                else if (info < node->info)
                    node = node->left;
                else
                    node = node->right;
            }

            node = new Node{info, 0, 0};

            //insere o nó
            if(!root)
                root = node;
            else if(info < prev->info)
                prev->left = node;
            else prev->right = node;

        }
        
        //deletando por root
        void erase(int info){
            Node** node = &root;

            while(*node){
                if((*node)->info == info)
                    break;
                
                if(info < (*node)->info)
                    node = &(*node)->left;
                else
                    node = &(*node)->right;
            }
            delete_by_merging(node);
        }

        //pesquisando tamanho
        int size() const{return size(root);}

        //algoritmo de busca
        bool search(int info) const { return search(root,info);}
};

int main()
{
    return 0;
}
```

```cpp
#include <iostream>
#include <functional>
//visitar o nó(V)
//realizar a travessia a esquerda(L)
//realizar a travessia a direito(R)
//1. pre-ordem: VLR
//2. em-ordem: LVR
//3. pós-ordem: LRV

class BST{
    private:
    struct Node{
        int info;
        Node *left, *right;
    };
    Node *root;

    void preorder(Node *node, function<void(Node*)>& visit){
        if(node){
            visit(node);
            preorder(node->left, visit);
            preorder(node->right, visit);
        }
    }

    void inorder(Node *node, function<void(Node*)>& visit){
        if(node){
            inorder(node->left, visit);
            visit(node);
            inorder(node->right,visit);
        }
    }

    void postorder(Node *node, function<void(Node*)>& visit){
        if(node){
            postorder(node->left,visit);
            postorder(node->right,visit);
            visit(node);
        }
    }
};

//para construir usar pre-ordem e em-ordem
```
```cpp
// problema de inserção de arvore binaria, com ordenação inorder, pre-ordem e pos-ordem

#include <iostream>

struct BST{
    struct  Node
    {
        int info;
        Node *left, *right;
    };

    Node *root;

    BST() : root(nullptr) {}

    void inorder(const Node* node)const{
        if(node){
            inorder(node->left);
            std::cout << ' ' << node ->info;
            inorder(node->right);
        }
    }

    void preorder(const Node* node)const{
        if(node){
            std::cout << ' ' << node->info;
            preorder(node->left);
            preorder(node->right);
        }
    }

    void postorder(const Node* node) const{
        if(node){
            postorder(node->left);
            postorder(node->right);
            std::cout << ' ' << node->info;
        }
    }

    void inser(int info){
        Node **node = &root;

        while(*node){
            if((*node)->info==info)
                return;
            else if(info <(*node)->info)
                node =  &(*node)->left;
            else
                node = &(*node)->right;
        }
        *node = new Node{info,nullptr ,nullptr};
    }

};

int main(){
    std::ios::sync_with_stdio(false);

    int C;
    std::cin >> C;

    for(int test = 1; test <= C; ++test){
        int N;
        std::cin >> N;

        BST tree;

        while (N--){
            int info;
            std::cin >> info;

            tree.insert(info);
        }
        std::cout << "Case " << test << ":\n";

        std::cout << "Pre.:";
        tree.preorder(tree.root);
        std::cout << "\n";

        std::cout << "In..:";
        tree.inorder(tree.root);
        std::cout << "\n";

        std::cout << "Post:";
        tree.postorder(tree.root);
        std::cout << "\n";

    }
    return 0;
}
```
