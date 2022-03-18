package Part03_SimpleSorting.Examples;

class ArraysIns {
    private long[] a;
    private int nElems;

    public ArraysIns(int max) {
        a = new long[max];
        nElems = 0;
    }

    public void insert(long value) {
        a[nElems] = value;
        nElems++;
    }

    public void display() {
        for (int i=0; i<nElems; i++)
            System.out.print(a[i] + " ");
        System.out.println("");
    }

    public void insertionSort() {
        int in, out;

        for (out=1; out<nElems; out++) {
            long temp = a[out];
            in = out;
            while (in>0 && a[in-1] >= temp) {
                a[in] = a[in-1];
                --in;
            }
            a[in] = temp;
        }
    }
}

class InsertSortApp {
    public static void main(String[] args) {
        int maxSize = 100;
        ArraysIns arr;
        arr = new ArraysIns(maxSize);

        arr.insert(77);
        arr.insert(99);
        arr.insert(44);
        arr.insert(55);
        arr.insert(22);
        arr.insert(88);
        arr.insert(11);
        arr.insert(0);
        arr.insert(66);
        arr.insert(33);

        arr.display();

        arr.insertionSort();

        arr.display();



    }
}
