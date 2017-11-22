import Data.List

subset::[a] ->[[a]]
subset [] = [[]]
subset (x:xs) = subset xs ++ map (x:)  (subset xs) 



combination :: [a] -> Int -> [[a]]
combination _   0    = [[]]
combination []  _    = []
combination (x:xs) n = ( map (x:)  (combination xs (n-1)) ) ++ combination xs n

fun ::(Num a, Ord a ) => [a] -> [a] -> Bool
fun y x = 
   case intersect y x == []  of 
         True ->   if ( if l_a > l_b then s_a > s_b else if l_a < l_b then  s_a < s_b else s_a /= s_b )  then True else False 
                   where 
                        s_a = sum y 
                        s_b = sum x 
                        l_a = length y
                        l_b = length x 
         _    -> True

checkOptimum ::(Num a , Ord a ) => [a] -> Bool
checkOptimum xs = optimumHelper  (sortBy (\a b -> compare ( sum a ) ( sum b) ) . tail.subset $ xs )  
                  where optimumHelper [x,y] = if fun x y then True else False
                        optimumHelper  (x:y:ys)  = if fun x y  then optimumHelper  (y:ys) else False 





main = do 
       let lst_1 = filter checkOptimum $ combination [20..45] 7
           ans = foldl' (\(acc , list )  x -> if  sum x  < acc then ( sum x  , x )  else ( acc , list) ) ( 1000 , [] ) lst_1
       print ans
