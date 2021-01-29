int trappingWater(int arr[], int n){

    // Your code here
    int left_max[n-2] = {arr[0]}, right_max[n-2] = {0}, total_water_trapped = 0;
    right_max[n-3] = arr[n-1]; 
    
    for(int i = 1; i < n-2 ; i++)
    {
        if(arr[i] > left_max[i-1])
        {
            left_max[i] = arr[i];
        }
        else
        {
            left_max[i] = left_max[i-1];
        }
    }

    for(int i = n-2; i > 1; i--)
    {
        if(arr[i] > right_max[i-1])
        {
            right_max[i-2] = arr[i];
        }
        else
        {
            right_max[i-2] = right_max[i-1];
        }
    }
    
    for(int i = 1; i < n-1; i++)
    {
        int temp =  min(left_max[i-1], right_max[i-1]) - arr[i];
        // cout<<temp<<endl;
        if(temp > 0)
            total_water_trapped = total_water_trapped + temp;
    }
    return total_water_trapped;
}

// https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1#
// https://practice.geeksforgeeks.org/viewSol.php?subId=8264617b0bef06a6b32368a14fafe87e&pid=701211&user=brighterbee
