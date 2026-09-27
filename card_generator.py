import random
import string
from datetime import datetime, timedelta
from typing import Dict, Tuple


class DebitCardGenerator:
    """Generate and validate test/dummy debit card numbers with realistic data."""
    
    # Card issuer prefixes (BIN - Bank Identification Number)
    VISA_PREFIX = "4"
    MASTERCARD_PREFIX = "5"
    AMEX_PREFIX = "3"
    DISCOVER_PREFIX = "6"
    
    # Card issuer lengths
    CARD_LENGTHS = {
        "VISA": 16,
        "MASTERCARD": 16,
        "AMEX": 15,
        "DISCOVER": 16
    }
    
    @staticmethod
    def luhn_checksum(card_number: str) -> int:
        """Calculate Luhn checksum for card validation."""
        def digits_of(n):
            return [int(d) for d in str(n)]
        
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        
        return checksum % 10
    
    @staticmethod
    def generate_card_number(card_type: str = "VISA") -> str:
        """
        Generate a valid card number using Luhn algorithm.
        
        Args:
            card_type: Type of card (VISA, MASTERCARD, AMEX, DISCOVER)
            
        Returns:
            Valid card number string
        """
        card_type = card_type.upper()
        
        if card_type not in DebitCardGenerator.CARD_LENGTHS:
            raise ValueError(f"Card type must be one of {list(DebitCardGenerator.CARD_LENGTHS.keys())}")
        
        # Select prefix based on card type
        if card_type == "VISA":
            prefix = DebitCardGenerator.VISA_PREFIX
        elif card_type == "MASTERCARD":
            prefix = DebitCardGenerator.MASTERCARD_PREFIX
        elif card_type == "AMEX":
            prefix = DebitCardGenerator.AMEX_PREFIX
        else:  # DISCOVER
            prefix = DebitCardGenerator.DISCOVER_PREFIX
        
        # Generate random digits
        length = DebitCardGenerator.CARD_LENGTHS[card_type] - 1
        card_number = prefix + ''.join([str(random.randint(0, 9)) for _ in range(length - 1)])
        
        # Add Luhn checksum
        checksum = DebitCardGenerator.luhn_checksum(card_number + "0")
        check_digit = (10 - checksum) % 10
        
        return card_number + str(check_digit)
    
    @staticmethod
    def generate_expiry_date(years_ahead: int = 5) -> str:
        """
        Generate a future expiry date in MM/YY format.
        
        Args:
            years_ahead: Number of years in the future (default: 5)
            
        Returns:
            Expiry date as MM/YY string
        """
        future_date = datetime.now() + timedelta(days=random.randint(1, 365 * years_ahead))
        month = str(future_date.month).zfill(2)
        year = str(future_date.year)[-2:]
        return f"{month}/{year}"
    
    @staticmethod
    def generate_cvv(card_type: str = "VISA") -> str:
        """
        Generate a CVV (Card Verification Value).
        AMEX uses 4 digits, all others use 3 digits.
        
        Args:
            card_type: Type of card (VISA, MASTERCARD, AMEX, DISCOVER)
            
        Returns:
            CVV as string
        """
        card_type = card_type.upper()
        length = 4 if card_type == "AMEX" else 3
        return ''.join([str(random.randint(0, 9)) for _ in range(length)])
    
    @staticmethod
    def generate_cardholder_name() -> str:
        """
        Generate a random cardholder name.
        
        Returns:
            Full name as string
        """
        first_names = [
            "James", "Mary", "Robert", "Patricia", "Michael", "Jennifer",
            "William", "Linda", "David", "Barbara", "Richard", "Susan",
            "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen"
        ]
        last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
            "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez",
            "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore"
        ]
        
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        return f"{first_name} {last_name}"
    
    @staticmethod
    def validate_card_number(card_number: str) -> bool:
        """
        Validate a card number using Luhn algorithm.
        
        Args:
            card_number: Card number to validate
            
        Returns:
            True if valid, False otherwise
        """
        if not card_number.isdigit():
            return False
        
        checksum = DebitCardGenerator.luhn_checksum(card_number)
        return checksum == 0
    
    @staticmethod
    def validate_expiry_date(expiry_date: str) -> bool:
        """
        Validate expiry date format and check if not expired.
        
        Args:
            expiry_date: Expiry date in MM/YY format
            
        Returns:
            True if valid and not expired, False otherwise
        """
        try:
            month, year = expiry_date.split("/")
            month = int(month)
            year = int(year)
            
            if month < 1 or month > 12:
                return False
            
            # Assume 20XX for 2-digit year
            full_year = 2000 + year if year < 100 else year
            expiry = datetime(full_year, month, 1)
            
            # Check if not expired (considering end of month)
            return expiry > datetime.now()
        except (ValueError, AttributeError):
            return False
    
    @staticmethod
    def validate_cvv(cvv: str, card_type: str = "VISA") -> bool:
        """
        Validate CVV format.
        
        Args:
            cvv: CVV to validate
            card_type: Type of card (VISA, MASTERCARD, AMEX, DISCOVER)
            
        Returns:
            True if valid, False otherwise
        """
        card_type = card_type.upper()
        expected_length = 4 if card_type == "AMEX" else 3
        
        return cvv.isdigit() and len(cvv) == expected_length
    
    @staticmethod
    def generate_card(card_type: str = "VISA") -> Dict[str, str]:
        """
        Generate complete dummy card data.
        
        Args:
            card_type: Type of card (VISA, MASTERCARD, AMEX, DISCOVER)
            
        Returns:
            Dictionary containing card data
        """
        return {
            "card_type": card_type.upper(),
            "card_number": DebitCardGenerator.generate_card_number(card_type),
            "cardholder_name": DebitCardGenerator.generate_cardholder_name(),
            "expiry_date": DebitCardGenerator.generate_expiry_date(),
            "cvv": DebitCardGenerator.generate_cvv(card_type)
        }
    
    @staticmethod
    def print_card(card_data: Dict[str, str]) -> None:
        """Pretty print card data."""
        print("\n" + "="*50)
        print(f"Card Type:       {card_data['card_type']}")
        print(f"Card Number:     {card_data['card_number']}")
        print(f"Cardholder:      {card_data['cardholder_name']}")
        print(f"Expiry Date:     {card_data['expiry_date']}")
        print(f"CVV:             {card_data['cvv']}")
        print("="*50 + "\n")


if __name__ == "__main__":
    # Example usage
    generator = DebitCardGenerator()
    
    # Generate a single card
    card = generator.generate_card("VISA")
    generator.print_card(card)
    
    # Generate multiple cards
    print("Generating 3 MasterCard cards:\n")
    for i in range(3):
        card = generator.generate_card("MASTERCARD")
        generator.print_card(card)
    
    # Validate cards
    print("Card Validation Tests:")
    test_card = generator.generate_card("AMEX")
    print(f"Card Number Valid: {generator.validate_card_number(test_card['card_number'])}")
    print(f"Expiry Date Valid: {generator.validate_expiry_date(test_card['expiry_date'])}")
    print(f"CVV Valid: {generator.validate_cvv(test_card['cvv'], 'AMEX')}")
