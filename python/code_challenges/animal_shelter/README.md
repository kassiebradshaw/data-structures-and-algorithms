# Code Challenge 12 - Animal Shelter

Author: *Kassie Bradshaw*

[Link to PR](https://github.com/kassiebradshaw/data-structures-and-algorithms/pull/33)

---

## Overview

First-In, First-Out Animal Shelter

**Challenge Type**: Code Challenge / Algorithm

---

## Feature Tasks

* [ ] Create a class called AnimalShelter which holds only dogs and cats
* [ ] The shelter operates using a *first-in, first-out* approach
* [ ] Implement the following methods:
  * [ ] **enqueue**
    * *Arguments*: `animal`
      * `animal` can be either a `"dog"` or `"cat"` object
  * [ ] **dequeue**
    * *Arguments*: `pref` (either `"dog"` or `"cat"`)
    * *Return*: either a dog or cat, based on preference
      * if `pref` is not `"dog"` or `"cat"` then return null

---

## Stretch Goals

If a cat or dog isn't preferred, return whichever animal has been waiting in the shelter the longest

---

## Testing
