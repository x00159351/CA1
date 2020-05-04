package main

import (
	"fmt"
	"log"
    "net/http"
    "math/rand"
    "strconv"
)

var i int
var increment int = 15
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