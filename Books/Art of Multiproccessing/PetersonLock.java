class PetersonLock implements Lock {
// thread-local index, 0 or 1
private volatile boolean[] flag = new boolean[2];
private volatile int victim;
public void lock() {
int i = ThreadID.get();
int j = 1 - i;
flag[i] = true;
// I’m interested
victim = i;
// you go first
while (flag[j] && victim == i) {}; // wait
}
public void unlock() {
int i = ThreadID.get();
flag[i] = false;
// I’m not interested
}
}
