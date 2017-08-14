# GitPitch testing

---

## Slide fragments

+++

### Unordered lists

```

- List item 1
- List item 2 |
- List item 3 |

```

- List item 1
- List item 2 |
- List item 3 |

+++

### Ordered Lists

```

1. List item 1
1. List item 2 |
1. List item 3 |

```

1. List item 1
1. List item 2 |
1. List item 3 |

+++

### Unordered list with markdown

```

- _First_ list item
- _Second_ list item |
- List item _three_ |

```

- _First_ list item
- _Second_ list item |
- List item _three_ |

+++

### Ordered Lists with full fragment syntax

```

1. List item 1
1. List item 2 <!-- .element: class="fragment" -->
1. List item 3 <!-- .element: class="fragment" -->

```

1. List item 1
1. List item 2 <!-- .element: class="fragment" -->
1. List item 3 <!-- .element: class="fragment" -->

+++

### Unordered list with markdown with full fragment syntax

```

- _First_ list item
- _Second_ list item <!-- .element: class="fragment" -->
- List item _three_ <!-- .element: class="fragment" -->

```

- _First_ list item
- _Second_ list item <!-- .element: class="fragment" -->
- List item _three_ <!-- .element: class="fragment" -->

+++

### Text blocks

```

Here is a line of text.

Here is another one in a fragment using the pipe syntax. |

Here is another fragment using the full syntax. <!-- .element: class="fragment" -->

*Here* is a text block with some markdown formatting and a pipe. |

And *here* is a corresponding one with the full syntax. <!-- .element: class="fragment" -->

```

Here is a line of text.

Here is another one in a fragment using the pipe syntax. |

Here is another fragment using the full syntax. <!-- .element: class="fragment" -->

*Here* is a text block with some markdown formatting and a pipe. |

And *here* is a corresponding one with the full syntax. <!-- .element: class="fragment" -->

+++

### Text blocks

```

<p>Let's try that again.</p>
<p>Here is a fragment.</p><!-- .element: class="fragment" -->
<p>Here is <em>another</em> fragment.</p> <!-- .element: class="fragment" -->
<p>And <strong>here</strong> is yet another fragment.</p> <!-- .element: class="fragment" -->
<p>I am explicitly inserting html formatting here.</p> <!-- .element: class="fragment" -->

```

<p>Let's try that again.</p>
<p>Here is a fragment.</p><!-- .element: class="fragment" -->
<p>Here is <em>another</em> fragment.</p> <!-- .element: class="fragment" -->
<p>And <strong>here</strong> is yet another fragment.</p> <!-- .element: class="fragment" -->
<p>I am explicitly inserting html formatting here.</p> <!-- .element: class="fragment" -->

+++

### Unordered markdown lists with explicit html formatting and pipes

```

- <strong>First</strong> list item
- <strong>Second</strong> list item |
- List item <strong>three</strong> |

```

- <strong>First</strong> list item
- <strong>Second</strong> list item |
- List item <strong>three</strong> |

+++

### Unordered markdown lists with explicit html formatting and full fragment syntax

```

- <strong>First</strong> list item
- <strong>Second</strong> list item <!-- .element: class="fragment" -->
- List item <strong>three</strong> <!-- .element: class="fragment" -->

```

- <strong>First</strong> list item
- <strong>Second</strong> list item <!-- .element: class="fragment" -->
- List item <strong>three</strong> <!-- .element: class="fragment" -->

+++

### Unordered _html_ lists with explicit html formatting and pipes

```

<ul>
<li><strong>First</strong> list item </li>|
<li><strong>Second</strong> list item</li>|
<li>List item <strong>three</strong> </li>|
</ul>

```

<ul>
<li><strong>First</strong> list item </li>|
<li><strong>Second</strong> list item</li>|
<li>List item <strong>three</strong> </li>|
</ul>

+++

### Unordered _html_ lists with explicit html formatting and full fragment syntax

```

<ul>
<li><strong>First</strong> list item </li><!-- .element: class="fragment" -->
<li><strong>Second</strong> list item</li><!-- .element: class="fragment" -->
<li>List item <strong>three</strong> </li><!-- .element: class="fragment" -->
</ul>

```

<ul>
<li><strong>First</strong> list item </li><!-- .element: class="fragment" -->
<li><strong>Second</strong> list item</li><!-- .element: class="fragment" -->
<li>List item <strong>three</strong> </li><!-- .element: class="fragment" -->
</ul>
