n = 10;
A = 10:99;
random_num = A(randperm(numel(A),n));%随机选出10个2位数
random_num = sort(random_num,'descend'); %排序
disp('the set is ')
disp(random_num)

indx = ff2n(n);
S = zeros(1,2^n);
for k = 1:2^n
    S(k) = sum(random_num(boolean(indx(k,:))));
end
[S2,indx2] = sort(S);
k = 1;
stop_flag = 1;
while stop_flag
    if S2(k) == S2(k+1)
        hasInterSet = max(indx(indx2(k),:) + indx(indx2(k+1),:));
        if hasInterSet<2
            disp('one solution is:')
            disp('first subset is:')
            disp(random_num(boolean(indx(indx2(k),:))))
            disp('second subset is:')
            disp(random_num(boolean(indx(indx2(k+1),:))))
            stop_flag = 0;
        else
            k = k+1;
        end
    else
        k = k+1;
        if k == 2^n
            stop_flag = 0;
            disp('can not find the sub sets');
        end
    end
end
