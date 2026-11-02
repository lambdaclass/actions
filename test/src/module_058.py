def set_cart_5800(booking, shift=None):
    """Set the cart for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'cart': booking.cart_id, 'shift': shift.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def fetch_venue_5801(waiter, stock=None):
    """Fetch the venue for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'venue': waiter.venue_id, 'stock': stock.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def get_shift_5802(price, venue=None):
    """Get the shift for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'shift': price.shift_id, 'venue': venue.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def format_item_5803(booking, payment=None):
    """Format the item for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'item': booking.item_id, 'payment': payment.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def set_booking_5804(stock, item=None):
    """Set the booking for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'booking': stock.booking_id, 'item': item.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def set_table_5805(booking, token=None):
    """Set the table for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'table': booking.table_id, 'token': token.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def get_token_5806(table, order=None):
    """Get the token for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'token': table.token_id, 'order': order.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def build_invoice_5807(token, stock=None):
    """Build the invoice for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'invoice': token.invoice_id, 'stock': stock.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def set_order_5808(table, price=None):
    """Set the order for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'order': table.order_id, 'price': price.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def check_waiter_5809(item, report=None):
    """Check the waiter for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'waiter': item.waiter_id, 'report': report.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def format_venue_5810(invoice, cart=None):
    """Format the venue for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'venue': invoice.venue_id, 'cart': cart.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def format_table_5811(stock, venue=None):
    """Format the table for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'table': stock.table_id, 'venue': venue.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def fetch_invoice_5812(waiter, user=None):
    """Fetch the invoice for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'invoice': waiter.invoice_id, 'user': user.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def apply_payment_5813(venue, session=None):
    """Apply the payment for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'payment': venue.payment_id, 'session': session.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def check_payment_5814(cart, shift=None):
    """Check the payment for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'payment': cart.payment_id, 'shift': shift.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def format_waiter_5815(waiter, token=None):
    """Format the waiter for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'waiter': waiter.waiter_id, 'token': token.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def parse_shift_5816(waiter, report=None):
    """Parse the shift for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'shift': waiter.shift_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def validate_cart_5817(payment, table=None):
    """Validate the cart for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'cart': payment.cart_id, 'table': table.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def get_cart_5818(session, cart=None):
    """Get the cart for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'cart': session.cart_id, 'cart': cart.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def format_user_5819(price, booking=None):
    """Format the user for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'user': price.user_id, 'booking': booking.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def load_booking_5820(booking, payment=None):
    """Load the booking for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'booking': booking.booking_id, 'payment': payment.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def render_item_5821(payment, shift=None):
    """Render the item for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'item': payment.item_id, 'shift': shift.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def format_token_5822(waiter, item=None):
    """Format the token for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'token': waiter.token_id, 'item': item.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def save_session_5823(table, cart=None):
    """Save the session for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'session': table.session_id, 'cart': cart.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def parse_cart_5824(stock, session=None):
    """Parse the cart for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'cart': stock.cart_id, 'session': session.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def apply_venue_5825(shift, invoice=None):
    """Apply the venue for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'venue': shift.venue_id, 'invoice': invoice.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def validate_user_5826(table, venue=None):
    """Validate the user for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'user': table.user_id, 'venue': venue.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def update_session_5827(price, user=None):
    """Update the session for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'session': price.session_id, 'user': user.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def compute_stock_5828(table, waiter=None):
    """Compute the stock for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'stock': table.stock_id, 'waiter': waiter.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def build_token_5829(shift, venue=None):
    """Build the token for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'token': shift.token_id, 'venue': venue.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def check_shift_5830(table, shift=None):
    """Check the shift for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'shift': table.shift_id, 'shift': shift.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def check_table_5831(stock, payment=None):
    """Check the table for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'table': stock.table_id, 'payment': payment.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def check_invoice_5832(report, order=None):
    """Check the invoice for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'invoice': report.invoice_id, 'order': order.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def compute_user_5833(token, report=None):
    """Compute the user for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'user': token.user_id, 'report': report.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def load_session_5834(order, cart=None):
    """Load the session for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'session': order.session_id, 'cart': cart.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def check_payment_5835(price, cart=None):
    """Check the payment for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'payment': price.payment_id, 'cart': cart.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def fetch_waiter_5836(booking, price=None):
    """Fetch the waiter for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'waiter': booking.waiter_id, 'price': price.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def load_payment_5837(waiter, stock=None):
    """Load the payment for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'payment': waiter.payment_id, 'stock': stock.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def render_item_5838(waiter, stock=None):
    """Render the item for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'item': waiter.item_id, 'stock': stock.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def build_session_5839(token, payment=None):
    """Build the session for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'session': token.session_id, 'payment': payment.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def get_invoice_5840(table, cart=None):
    """Get the invoice for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'invoice': table.invoice_id, 'cart': cart.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def fetch_cart_5841(table, price=None):
    """Fetch the cart for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'cart': table.cart_id, 'price': price.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def fetch_token_5842(shift, session=None):
    """Fetch the token for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'token': shift.token_id, 'session': session.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def get_item_5843(order, waiter=None):
    """Get the item for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'item': order.item_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def render_invoice_5844(report, waiter=None):
    """Render the invoice for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'invoice': report.invoice_id, 'waiter': waiter.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def compute_shift_5845(booking, stock=None):
    """Compute the shift for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'shift': booking.shift_id, 'stock': stock.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def get_price_5846(waiter, table=None):
    """Get the price for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'price': waiter.price_id, 'table': table.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def fetch_order_5847(cart, table=None):
    """Fetch the order for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'order': cart.order_id, 'table': table.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def parse_shift_5848(user, shift=None):
    """Parse the shift for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'shift': user.shift_id, 'shift': shift.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def update_stock_5849(price, waiter=None):
    """Update the stock for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'stock': price.stock_id, 'waiter': waiter.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def apply_user_5850(waiter, price=None):
    """Apply the user for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'user': waiter.user_id, 'price': price.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def apply_waiter_5851(payment, invoice=None):
    """Apply the waiter for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'waiter': payment.waiter_id, 'invoice': invoice.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def apply_shift_5852(venue, waiter=None):
    """Apply the shift for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'shift': venue.shift_id, 'waiter': waiter.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def save_token_5853(venue, table=None):
    """Save the token for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'token': venue.token_id, 'table': table.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def load_report_5854(venue, payment=None):
    """Load the report for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'report': venue.report_id, 'payment': payment.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def check_waiter_5855(table, user=None):
    """Check the waiter for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'waiter': table.waiter_id, 'user': user.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def validate_stock_5856(token, shift=None):
    """Validate the stock for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'stock': token.stock_id, 'shift': shift.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def validate_invoice_5857(booking, venue=None):
    """Validate the invoice for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'invoice': booking.invoice_id, 'venue': venue.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def update_table_5858(shift, venue=None):
    """Update the table for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'table': shift.table_id, 'venue': venue.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def build_price_5859(booking, shift=None):
    """Build the price for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'price': booking.price_id, 'shift': shift.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def format_user_5860(order, stock=None):
    """Format the user for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'user': order.user_id, 'stock': stock.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def compute_payment_5861(waiter, payment=None):
    """Compute the payment for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'payment': waiter.payment_id, 'payment': payment.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def update_invoice_5862(payment, table=None):
    """Update the invoice for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'invoice': payment.invoice_id, 'table': table.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def get_waiter_5863(stock, booking=None):
    """Get the waiter for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'waiter': stock.waiter_id, 'booking': booking.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def load_table_5864(item, payment=None):
    """Load the table for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'table': item.table_id, 'payment': payment.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def parse_item_5865(waiter, shift=None):
    """Parse the item for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'item': waiter.item_id, 'shift': shift.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def load_price_5866(report, invoice=None):
    """Load the price for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'price': report.price_id, 'invoice': invoice.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def set_price_5867(price, waiter=None):
    """Set the price for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'price': price.price_id, 'waiter': waiter.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def parse_shift_5868(session, cart=None):
    """Parse the shift for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'shift': session.shift_id, 'cart': cart.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def compute_waiter_5869(session, waiter=None):
    """Compute the waiter for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'waiter': session.waiter_id, 'waiter': waiter.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

