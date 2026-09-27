# Debit Card Generator

A Python utility to generate test/dummy debit card numbers with realistic card data, validation, and formatting support.

⚠️ **DISCLAIMER**: This tool is for **testing and educational purposes only**. Generated card numbers are dummy/test values and should never be used for fraudulent activities or actual transactions.

## Features

✅ **Card Generation**
- Generate valid card numbers for VISA, MasterCard, American Express, and Discover
- Uses the Luhn algorithm to ensure generated card numbers are mathematically valid

✅ **Realistic Card Data**
- Random cardholder names
- Expiry dates (MM/YY format) with configurable future date range
- CVV/CVC generation (3 digits for most cards, 4 for AMEX)

✅ **Validation Methods**
- Validate card numbers using Luhn algorithm
- Verify expiry date format and check if expired
- Validate CVV format based on card type

✅ **Multiple Card Types**
- VISA (16 digits)
- MasterCard (16 digits)
- American Express (15 digits, 4-digit CVV)
- Discover (16 digits)

## Installation

Clone the repository:
```bash
git clone https://github.com/lilcorrupt2122-sketch/debit-card-generator.git
cd debit-card-generator
```

No external dependencies required! Uses only Python standard library.

## Usage

### Basic Usage

```python
from card_generator import DebitCardGenerator

# Generate a single VISA card
card = DebitCardGenerator.generate_card("VISA")
print(card)
# Output: {'card_type': 'VISA', 'card_number': '4532015112830366', 
#          'cardholder_name': 'James Smith', 'expiry_date': '12/28', 'cvv': '847'}
```

### Generate Different Card Types

```python
# Generate MasterCard
mastercard = DebitCardGenerator.generate_card("MASTERCARD")

# Generate American Express
amex = DebitCardGenerator.generate_card("AMEX")

# Generate Discover
discover = DebitCardGenerator.generate_card("DISCOVER")
```

### Generate Individual Components

```python
generator = DebitCardGenerator()

# Generate card number only
card_number = generator.generate_card_number("VISA")

# Generate expiry date (default: 5 years ahead)
expiry = generator.generate_expiry_date(years_ahead=3)

# Generate CVV
cvv = generator.generate_cvv("VISA")

# Generate cardholder name
name = generator.generate_cardholder_name()
```

### Validate Card Data

```python
# Validate card number
is_valid = DebitCardGenerator.validate_card_number("4532015112830366")  # True

# Validate expiry date
is_valid = DebitCardGenerator.validate_expiry_date("12/28")  # True (if not expired)

# Validate CVV
is_valid = DebitCardGenerator.validate_cvv("847", "VISA")  # True
```

### Pretty Print Card

```python
card = DebitCardGenerator.generate_card("VISA")
DebitCardGenerator.print_card(card)

# Output:
# ==================================================
# Card Type:       VISA
# Card Number:     4532015112830366
# Cardholder:      James Smith
# Expiry Date:     12/28
# CVV:             847
# ==================================================
```

## API Reference

### `DebitCardGenerator` Class

#### Static Methods

**`generate_card(card_type="VISA") -> Dict[str, str]`**
- Generate complete dummy card data
- **Parameters:**
  - `card_type` (str): Card type - "VISA", "MASTERCARD", "AMEX", or "DISCOVER"
- **Returns:** Dictionary with keys: `card_type`, `card_number`, `cardholder_name`, `expiry_date`, `cvv`

**`generate_card_number(card_type="VISA") -> str`**
- Generate a valid card number with Luhn checksum
- **Parameters:**
  - `card_type` (str): Card type
- **Returns:** Valid card number string

**`generate_expiry_date(years_ahead=5) -> str`**
- Generate future expiry date
- **Parameters:**
  - `years_ahead` (int): Number of years in the future
- **Returns:** Expiry date in MM/YY format

**`generate_cvv(card_type="VISA") -> str`**
- Generate CVV (3 digits for most cards, 4 for AMEX)
- **Parameters:**
  - `card_type` (str): Card type
- **Returns:** CVV string

**`generate_cardholder_name() -> str`**
- Generate random cardholder name
- **Returns:** Full name string

**`validate_card_number(card_number) -> bool`**
- Validate card number using Luhn algorithm
- **Parameters:**
  - `card_number` (str): Card number to validate
- **Returns:** True if valid, False otherwise

**`validate_expiry_date(expiry_date) -> bool`**
- Validate expiry date format and check if not expired
- **Parameters:**
  - `expiry_date` (str): Expiry date in MM/YY format
- **Returns:** True if valid and not expired, False otherwise

**`validate_cvv(cvv, card_type="VISA") -> bool`**
- Validate CVV format
- **Parameters:**
  - `cvv` (str): CVV to validate
  - `card_type` (str): Card type
- **Returns:** True if valid, False otherwise

**`print_card(card_data) -> None`**
- Pretty print card data
- **Parameters:**
  - `card_data` (dict): Card data dictionary

## Running Examples

Run the module directly to see example output:

```bash
python card_generator.py
```

This will generate sample cards and demonstrate validation.

## Card Details

### Supported Card Types

| Card Type     | Length | CVV Length | BIN Prefix |
|---------------|--------|------------|------------|
| VISA          | 16     | 3          | 4          |
| MasterCard    | 16     | 3          | 5          |
| American Express | 15  | 4          | 3          |
| Discover      | 16     | 3          | 6          |

### Luhn Algorithm

The Luhn algorithm is used to validate card numbers. All generated card numbers pass this validation:

1. Double every second digit from right to left
2. If doubling of a digit results in a two-digit number, add the digits together
3. Sum all the digits
4. If the total modulo 10 equals 0, the card number is valid

## Use Cases

- **Testing payment systems** during development
- **Unit testing** e-commerce applications
- **Educational purposes** to understand card validation
- **Demo applications** that require payment input
- **Security research** and testing (with permission)

## Disclaimer

⚠️ **This tool is for educational and testing purposes only.** 

- Do NOT use generated card numbers for actual transactions
- Do NOT use to commit fraud or any illegal activities
- Do NOT attempt to process these cards with real payment processors
- Generated data is entirely fictional

Unauthorized access to or use of computer systems is illegal. This tool should only be used on systems you own or have explicit permission to test.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## References

- [Luhn Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Luhn_algorithm)
- [Credit Card Industry Standards](https://en.wikipedia.org/wiki/Payment_card_number)
- [BIN Database](https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN))

## Support

For issues, questions, or suggestions, please open an [Issue](https://github.com/lilcorrupt2122-sketch/debit-card-generator/issues) on GitHub.
