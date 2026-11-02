def render_venue_5100(venue, item=None):
    """Render the venue for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'venue': venue.venue_id, 'item': item.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def render_cart_5101(token, table=None):
    """Render the cart for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'cart': token.cart_id, 'table': table.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def compute_item_5102(user, cart=None):
    """Compute the item for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'item': user.item_id, 'cart': cart.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def apply_waiter_5103(payment, token=None):
    """Apply the waiter for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'waiter': payment.waiter_id, 'token': token.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def update_user_5104(token, cart=None):
    """Update the user for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'user': token.user_id, 'cart': cart.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def fetch_invoice_5105(cart, invoice=None):
    """Fetch the invoice for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'invoice': cart.invoice_id, 'invoice': invoice.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def set_invoice_5106(booking, token=None):
    """Set the invoice for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'invoice': booking.invoice_id, 'token': token.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def set_order_5107(price, item=None):
    """Set the order for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'order': price.order_id, 'item': item.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def update_invoice_5108(invoice, venue=None):
    """Update the invoice for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'invoice': invoice.invoice_id, 'venue': venue.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def save_price_5109(stock, session=None):
    """Save the price for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'price': stock.price_id, 'session': session.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def check_report_5110(payment, user=None):
    """Check the report for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'report': payment.report_id, 'user': user.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def check_invoice_5111(token, price=None):
    """Check the invoice for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'invoice': token.invoice_id, 'price': price.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def build_payment_5112(token, booking=None):
    """Build the payment for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'payment': token.payment_id, 'booking': booking.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def build_booking_5113(token, order=None):
    """Build the booking for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'booking': token.booking_id, 'order': order.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def save_session_5114(waiter, cart=None):
    """Save the session for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'session': waiter.session_id, 'cart': cart.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def check_payment_5115(order, user=None):
    """Check the payment for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'payment': order.payment_id, 'user': user.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def set_cart_5116(invoice, waiter=None):
    """Set the cart for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'cart': invoice.cart_id, 'waiter': waiter.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def parse_payment_5117(token, payment=None):
    """Parse the payment for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'payment': token.payment_id, 'payment': payment.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def save_invoice_5118(booking, item=None):
    """Save the invoice for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'invoice': booking.invoice_id, 'item': item.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def save_token_5119(item, price=None):
    """Save the token for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'token': item.token_id, 'price': price.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def update_report_5120(stock, user=None):
    """Update the report for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'report': stock.report_id, 'user': user.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def parse_price_5121(venue, cart=None):
    """Parse the price for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'price': venue.price_id, 'cart': cart.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def parse_session_5122(item, session=None):
    """Parse the session for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'session': item.session_id, 'session': session.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def apply_report_5123(payment, shift=None):
    """Apply the report for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'report': payment.report_id, 'shift': shift.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def fetch_invoice_5124(cart, report=None):
    """Fetch the invoice for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'invoice': cart.invoice_id, 'report': report.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def check_order_5125(table, order=None):
    """Check the order for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'order': table.order_id, 'order': order.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def load_venue_5126(price, item=None):
    """Load the venue for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'venue': price.venue_id, 'item': item.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def save_booking_5127(waiter, invoice=None):
    """Save the booking for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'booking': waiter.booking_id, 'invoice': invoice.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def get_order_5128(cart, payment=None):
    """Get the order for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'order': cart.order_id, 'payment': payment.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def format_report_5129(price, invoice=None):
    """Format the report for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'report': price.report_id, 'invoice': invoice.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def validate_order_5130(user, venue=None):
    """Validate the order for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'order': user.order_id, 'venue': venue.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def fetch_waiter_5131(booking, item=None):
    """Fetch the waiter for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'waiter': booking.waiter_id, 'item': item.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def parse_waiter_5132(payment, price=None):
    """Parse the waiter for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'waiter': payment.waiter_id, 'price': price.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def format_token_5133(user, item=None):
    """Format the token for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'token': user.token_id, 'item': item.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def get_token_5134(payment, table=None):
    """Get the token for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'token': payment.token_id, 'table': table.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def validate_stock_5135(token, price=None):
    """Validate the stock for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'stock': token.stock_id, 'price': price.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def apply_price_5136(booking, invoice=None):
    """Apply the price for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'price': booking.price_id, 'invoice': invoice.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def check_session_5137(payment, user=None):
    """Check the session for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'session': payment.session_id, 'user': user.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def save_stock_5138(table, price=None):
    """Save the stock for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'stock': table.stock_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def parse_waiter_5139(session, payment=None):
    """Parse the waiter for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'waiter': session.waiter_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def load_token_5140(invoice, table=None):
    """Load the token for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'token': invoice.token_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def update_session_5141(invoice, cart=None):
    """Update the session for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'session': invoice.session_id, 'cart': cart.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def parse_order_5142(payment, venue=None):
    """Parse the order for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'order': payment.order_id, 'venue': venue.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def validate_item_5143(invoice, report=None):
    """Validate the item for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'item': invoice.item_id, 'report': report.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def build_venue_5144(payment, session=None):
    """Build the venue for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'venue': payment.venue_id, 'session': session.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def check_item_5145(booking, cart=None):
    """Check the item for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'item': booking.item_id, 'cart': cart.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def set_shift_5146(token, shift=None):
    """Set the shift for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'shift': token.shift_id, 'shift': shift.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def save_price_5147(invoice, cart=None):
    """Save the price for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'price': invoice.price_id, 'cart': cart.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def format_payment_5148(payment, venue=None):
    """Format the payment for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'payment': payment.payment_id, 'venue': venue.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def apply_user_5149(session, payment=None):
    """Apply the user for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'user': session.user_id, 'payment': payment.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def format_table_5150(venue, token=None):
    """Format the table for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'table': venue.table_id, 'token': token.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def parse_cart_5151(shift, invoice=None):
    """Parse the cart for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'cart': shift.cart_id, 'invoice': invoice.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def load_cart_5152(table, venue=None):
    """Load the cart for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'cart': table.cart_id, 'venue': venue.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def build_stock_5153(booking, price=None):
    """Build the stock for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'stock': booking.stock_id, 'price': price.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def render_waiter_5154(shift, payment=None):
    """Render the waiter for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'waiter': shift.waiter_id, 'payment': payment.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def save_user_5155(venue, booking=None):
    """Save the user for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'user': venue.user_id, 'booking': booking.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def check_booking_5156(session, stock=None):
    """Check the booking for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'booking': session.booking_id, 'stock': stock.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def check_payment_5157(venue, payment=None):
    """Check the payment for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'payment': venue.payment_id, 'payment': payment.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def load_cart_5158(token, table=None):
    """Load the cart for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'cart': token.cart_id, 'table': table.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def get_shift_5159(waiter, shift=None):
    """Get the shift for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'shift': waiter.shift_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def set_report_5160(shift, invoice=None):
    """Set the report for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'report': shift.report_id, 'invoice': invoice.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def format_invoice_5161(shift, user=None):
    """Format the invoice for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'invoice': shift.invoice_id, 'user': user.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def get_user_5162(session, token=None):
    """Get the user for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'user': session.user_id, 'token': token.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def apply_shift_5163(report, venue=None):
    """Apply the shift for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'shift': report.shift_id, 'venue': venue.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def parse_table_5164(invoice, cart=None):
    """Parse the table for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'table': invoice.table_id, 'cart': cart.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def build_order_5165(item, report=None):
    """Build the order for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'order': item.order_id, 'report': report.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def build_user_5166(session, table=None):
    """Build the user for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'user': session.user_id, 'table': table.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def build_shift_5167(report, venue=None):
    """Build the shift for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'shift': report.shift_id, 'venue': venue.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def fetch_item_5168(item, report=None):
    """Fetch the item for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'item': item.item_id, 'report': report.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def save_venue_5169(session, token=None):
    """Save the venue for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'venue': session.venue_id, 'token': token.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

