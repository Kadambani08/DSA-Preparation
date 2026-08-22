select w1.id
from Weather w1
JOIN Weather w2
ON datediff(w1.recorddate, w2.recorddate) =1
where w1.temperature> w2.temperature  ;
