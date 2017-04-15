#lang racket


(define buildRange 
  (lambda (c1 c2)
    (cond
      ((>= c1 c2) null)
      (else (cons c1 (buildRange (+ 1 c1) c2))))))


(define problemOne
  (lambda ()
  (apply + (filter (lambda (x) (or (eq? (remainder x 3) 0) (eq? (remainder x 5) 0))) (buildRange 1 1000)))))