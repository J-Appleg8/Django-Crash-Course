# Scope Overview:

## Python follows the LEGB Rule:

If you define a variable name somewhere in your code, and then you want to call that variable further down then Python will look in the namespace - Which tells Python which variables go where.

The order in which Python seaches is:

- Local
- Enclosing Function locals
- Global
- Built in
<p></p>

---

L: Local

- Names assigned in any way within a function (def or lambda) and not declared global in that function

E: EFLs

- Name in teh local scope of any and all enclosing functions (def or lambda) from inner to outer

G: Global (module)

- Names assigned at the top-level of a module file, or declared global in a def within the file

B: Built-in (Python)

- Names pre-assigned in the built-in names module:
  - open, range, SyntaxError etc...
