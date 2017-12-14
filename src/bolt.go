package main

import (
	"C"
	"log"

	"github.com/boltdb/bolt"
)

//export Open
func Open() {
	db, err := bolt.Open("my.db", 0600, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()
}

func main() {}
