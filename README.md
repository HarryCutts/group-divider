# Group Divider

A simple Python script that takes one or two lists of people and randomly assigns them to groups. I use it, with a manual tweak or two afterwards, to create prayer groups within our Bible study group that can easily be reshuffled on a regular basis to keep things fresh.

## Usage

Pass the script a list of names:

```
Zoe
Jake
Trevor
Benjamin
...
```

And the sizes of the groups you want:

```
$ ./group_divider.py names.txt --group-sizes=5,4,4,4,4
Group 0: Diana, Vladimir, Kevin, Claire, Jake
Group 1: Zoe, Carl, Chani, Frank
Group 2: Trevor, Sebastian, Benjamin, Helen
Group 3: Deirdre, Rebecca, Lauren, Angela
Group 4: Simon, Stilgar, Christian, Paul
```

### Leaders

You can pass a separate set of leaders (in the same one-per-line format), people who will be assigned in order to the groups. For example, with a leaders file containing (with these names removed from `names.txt`):

```
Paul
Vladimir
Stilgar
Helen
```

```bash
$ ./group_divider.py names.txt leaders.txt --group-sizes=5,4,4,4,4
Group 0: Paul, Angela, Trevor, Claire, Diana
Group 1: Vladimir, Carl, Christian, Sebastian
Group 2: Stilgar, Simon, Benjamin, Chani
Group 3: Helen, Rebecca, Deirdre, Lauren
Group 4: Zoe, Kevin, Jake, Frank
```

### Inseparable people

If you want certain people to always be in the same group (for example, couples or people who use the same computer for video conferencing), you can separate their names with `&`:

```
Zoe & Jake
Trevor
Benjamin
Frank
...
```

```
$ ./group_divider.py names-with-couples.txt --group-sizes=5,4,4,4,4
Group 0: Zoe & Jake, Benjamin, Simon, Lauren
Group 1: Chani & Paul, Deirdre, Diana
Group 2: Angela & Claire, Helen, Frank
Group 3: Rebecca & Christian, Kevin, Sebastian
Group 4: Vladimir, Carl, Stilgar, Trevor
```
