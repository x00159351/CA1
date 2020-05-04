package main

import (
	"fmt"
	"log"
    "net/http"
    "math/rand"
    "strconv"
)

var i int = 7
var increment int = 10
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, strconv.Itoa(SetGetNumber()))
}

func SetGetNumber() (int) {
        i = i + rand.Intn(increment)
        return i
}
func main() {
    http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8888", nil))
}