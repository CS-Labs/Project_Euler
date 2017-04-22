$sum = 0

For ($i = 1; $i -lt 1000; $i++){
	if(($i%3 -eq 0) -Or ($i%5 -eq 0)){
		$sum = $sum + $i
	}
}

echo $sum