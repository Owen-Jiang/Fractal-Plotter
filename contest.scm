;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Your title here>
;;;
;;; Description:
;;;   <It's your masterpiece.
;;;    Use these three lines to describe
;;;    its inner meaning.>
(define (for i n fn)
	(if (< i n) 
		(begin 
			(fn i) 
			(for (+ i 1) n fn)
		)
		#t	
	)
)

(define (mandelbrot c)
	(print c)
	(lambda (z) (list (- (+ (car c) (* (car z) (car z))) (* (car (cdr z)) (car (cdr z)))) (+ (car (cdr c)) (* 2 (car z) (car (cdr z))))))
)

(define (iterate set-function n z)
	(if (= n 0)
		z
		(iterate set-function (- n 1) (set-function z))
	)
)

(define (c-abs z)
	(sqrt (+ (* (car z) (car z)) (* (car (cdr z)) (car (cdr z)))))
)

(define (converges? c set-function iter bound west east south north)
	(if (< (c-abs (iterate (set-function c) iter (list 0 0))) bound)
    	(pixel (* (quotient (screen_width) (- east west)) (car c)) (* (quotient (screen_width) (- north south)) (car (cdr c))) "black")
		(pixel (* (quotient (screen_width) (- east west)) (car c)) (* (quotient (screen_width) (- north south)) (car (cdr c))) "#00065e")
	)
)

(define (max x y)
	(if (> x y)
		x
		y
	)
)

(define (draw)
	(ht)
	(bgcolor "black")
	(speed 20000) ; delete later

	(define west -2)
	(define east 2)
	(define south -2)
	(define north 2)
	; (define resolution 0.002)
	(define resolution 0.01)

	(define ps (* 2 (/ (* resolution 1000) (max (- east west) (- north south))))) ; *2 to avoid the overlap lines
	(pixelsize ps)
	(pixel (- (quotient (screen_width) 2)) (- (quotient (screen_height) 2)) "green")
	
	(for (floor (/ west resolution)) (floor (/ east resolution)) (lambda (i) (pd) (for (floor (/ south resolution)) (floor (/ north resolution)) (lambda (j) (converges? (list (* i resolution) (* j resolution)) mandelbrot 9 2 west east south north))) (pu)))
	(exitonclick)	
)

; Please leave this last line alone. You may add additional procedures above
; this line.
(draw)