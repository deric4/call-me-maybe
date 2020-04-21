# Call-Me-Maybe 




## Why you might be interested

Lots of people talk about the importance of tests, but its not always easy to implement them in your own code.

I've found that most developers _(anyone that has to use a texteditor as part of their job junction)_ were not introduced to the world of development through the lens of needing to test or maintain code that serves any sort of business function.

A very popular repository on GitHub (over 100k :star:s!) is [@kamranahmedse's developer-roadmap](https://github.com/kamranahmedse/developer-roadmap).  

How far down the map do you have to go before you get to *testing*? Is this reflective of your learning experience?

_note: I've linked the 'Backend' roadmap, but other roadmaps have a similar journey_
<p align="center">
   <img  src="https://github.com/kamranahmedse/developer-roadmap/blob/master/img/backend.png">
</p>


<!-- Increase in Enterprise organization focusing on automation of tests -->
Digital Transformation -> means more work for developers

Many companies are currently or planning initiatives to adopt current industry practices, not because they want to use the "new & shiny" but because there's business value provided by adapting technologies and workflows which reduce delivery time.

...but they still want the "new & shiny" i.e. _Continous_ or _Automated_ ...


<p align="center">
  <figure>
    <a href=https://cdn.thenewstack.io/media/2019/12/e1fe2efe-tricentis1.png">
      <img src="https://cdn.thenewstack.io/media/2019/12/e1fe2efe-tricentis1.png">
    </a>
    <figcaption>The NewStack: Why Software Testing Remains A Bottleneck</figcaption>
  </figure>
</p>


Frequently this can make even the most minor of changes to an existing code base feeling like...
<p align="center">
<img src="https://media.giphy.com/media/MS0fQBmGGMaRy/giphy.gif">
</p>

There's a reason why no one's touched that code in _insert unit of time_

### Types of Testing

You'll hear following words thrown around quite a bit when talking about testing... and they can mean very different things depending on the context they're used. 

* unit
* functional
* integration
* end-to-end
* perfomance
* regression
* ...
* ...
* ...
* ...
* ...

For example, a unit test might mean something slightly different between developers who use live in different ecosystems (Python vs Java). What about between Data Scientists, SysAdmins, or Network Engineers.

* This may vary depending on what you're working on:
  - jupyter notebook
  - web application
  - cli tool
  - serverless function
  - library/package
* Code Structure
* Scope

It can feel a little bit like Calvinball at times :upside_down_face:.

<p>
  <img src="http://isaacbotkin.com/wp-content/uploads/2016/08/CalvinballOrganized.jpg">
</p>

### Testing Pyramid

One of the better talks I've come across with breaking down defintions not only across a language but across an Application's entire development lifecycle.

One of the best talks about testing (infrastructure) but principles can be applied generically.

[Automated Testing for Terraform, Docker, Packer, Kuberernetes, More](https://www.infoq.com/presentations/automated-testing-terraform-docker-packer/)


## Static Analyis

> "Look at my code, don't run it, tell me if there's a bug or if there's some sort of issue."

### Linters

* Flake8
* Pylint
* Pyflakes

### Formatters
* Black :star:
* isort

### Types
* MyPy
* Pydantic
* Marshmallow 

### Code Coverage
* Coverage.py

### Security
* Bandit


### Git
* pre-commit
* gitlint


## Unit Testing

Whats a unit?
<p>
  <img src="https://cdn.vox-cdn.com/thumbor/BQ-h-ALgc_6EFCWwPEV0Y_z6dSs=/0x0:1200x870/920x613/filters:focal(516x282:708x474)/cdn.vox-cdn.com/uploads/chorus_image/image/59535207/absolute_unit_sheep.0.jpg">

</p>

  it depends...

  Demo Time. What are the units in the demo app provided?

<p>
  <img src="docs/sequence.png">
</p>
## Pytest

IMHO the best python testing framework out there right now.



### Lab

Install pytest

```bash
$ python3 -m pip install --upgrade pip
$ python3 -m venv .venv
$ source .venv/bin/activate

# windows script path?
```


Verify

```bash
$ pytest -v
```
