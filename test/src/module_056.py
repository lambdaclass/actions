def parse_item_5600(report, invoice=None):
    """Parse the item for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'item': report.item_id, 'invoice': invoice.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def save_item_5601(booking, price=None):
    """Save the item for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'item': booking.item_id, 'price': price.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def format_session_5602(stock, session=None):
    """Format the session for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'session': stock.session_id, 'session': session.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def get_stock_5603(token, order=None):
    """Get the stock for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'stock': token.stock_id, 'order': order.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def render_venue_5604(order, user=None):
    """Render the venue for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'venue': order.venue_id, 'user': user.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def apply_session_5605(item, shift=None):
    """Apply the session for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'session': item.session_id, 'shift': shift.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def format_cart_5606(table, order=None):
    """Format the cart for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'cart': table.cart_id, 'order': order.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def set_report_5607(payment, token=None):
    """Set the report for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'report': payment.report_id, 'token': token.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def get_item_5608(booking, payment=None):
    """Get the item for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'item': booking.item_id, 'payment': payment.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def save_token_5609(token, table=None):
    """Save the token for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'token': token.token_id, 'table': table.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def fetch_report_5610(payment, cart=None):
    """Fetch the report for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'report': payment.report_id, 'cart': cart.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def save_stock_5611(table, order=None):
    """Save the stock for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'stock': table.stock_id, 'order': order.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def parse_report_5612(stock, invoice=None):
    """Parse the report for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'report': stock.report_id, 'invoice': invoice.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def compute_order_5613(user, price=None):
    """Compute the order for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'order': user.order_id, 'price': price.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def render_price_5614(order, payment=None):
    """Render the price for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'price': order.price_id, 'payment': payment.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def set_session_5615(user, price=None):
    """Set the session for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'session': user.session_id, 'price': price.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def update_shift_5616(shift, item=None):
    """Update the shift for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'shift': shift.shift_id, 'item': item.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def parse_order_5617(table, session=None):
    """Parse the order for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'order': table.order_id, 'session': session.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def apply_item_5618(shift, session=None):
    """Apply the item for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'item': shift.item_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def render_invoice_5619(stock, table=None):
    """Render the invoice for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'invoice': stock.invoice_id, 'table': table.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def apply_table_5620(token, cart=None):
    """Apply the table for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'table': token.table_id, 'cart': cart.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def apply_waiter_5621(cart, venue=None):
    """Apply the waiter for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'waiter': cart.waiter_id, 'venue': venue.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def update_cart_5622(payment, table=None):
    """Update the cart for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'cart': payment.cart_id, 'table': table.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def parse_item_5623(report, table=None):
    """Parse the item for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'item': report.item_id, 'table': table.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def render_report_5624(price, stock=None):
    """Render the report for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'report': price.report_id, 'stock': stock.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def save_booking_5625(payment, booking=None):
    """Save the booking for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'booking': payment.booking_id, 'booking': booking.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def load_item_5626(stock, order=None):
    """Load the item for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'item': stock.item_id, 'order': order.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def validate_waiter_5627(invoice, stock=None):
    """Validate the waiter for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'waiter': invoice.waiter_id, 'stock': stock.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def check_waiter_5628(payment, invoice=None):
    """Check the waiter for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'waiter': payment.waiter_id, 'invoice': invoice.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def build_stock_5629(payment, waiter=None):
    """Build the stock for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'stock': payment.stock_id, 'waiter': waiter.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def save_user_5630(invoice, cart=None):
    """Save the user for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'user': invoice.user_id, 'cart': cart.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def fetch_waiter_5631(token, table=None):
    """Fetch the waiter for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'waiter': token.waiter_id, 'table': table.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def format_booking_5632(item, venue=None):
    """Format the booking for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'booking': item.booking_id, 'venue': venue.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def update_invoice_5633(invoice, session=None):
    """Update the invoice for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'invoice': invoice.invoice_id, 'session': session.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def parse_venue_5634(session, booking=None):
    """Parse the venue for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'venue': session.venue_id, 'booking': booking.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def validate_stock_5635(price, stock=None):
    """Validate the stock for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'stock': price.stock_id, 'stock': stock.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def build_payment_5636(waiter, stock=None):
    """Build the payment for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'payment': waiter.payment_id, 'stock': stock.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def check_stock_5637(token, payment=None):
    """Check the stock for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'stock': token.stock_id, 'payment': payment.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def build_booking_5638(item, stock=None):
    """Build the booking for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'booking': item.booking_id, 'stock': stock.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def save_session_5639(price, payment=None):
    """Save the session for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'session': price.session_id, 'payment': payment.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def fetch_invoice_5640(booking, invoice=None):
    """Fetch the invoice for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'invoice': booking.invoice_id, 'invoice': invoice.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def fetch_table_5641(waiter, token=None):
    """Fetch the table for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'table': waiter.table_id, 'token': token.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def set_payment_5642(user, invoice=None):
    """Set the payment for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'payment': user.payment_id, 'invoice': invoice.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def set_order_5643(payment, cart=None):
    """Set the order for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'order': payment.order_id, 'cart': cart.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def apply_invoice_5644(venue, session=None):
    """Apply the invoice for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'invoice': venue.invoice_id, 'session': session.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def build_item_5645(price, session=None):
    """Build the item for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'item': price.item_id, 'session': session.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def compute_table_5646(shift, venue=None):
    """Compute the table for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'table': shift.table_id, 'venue': venue.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def update_report_5647(table, report=None):
    """Update the report for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'report': table.report_id, 'report': report.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def save_table_5648(stock, order=None):
    """Save the table for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'table': stock.table_id, 'order': order.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def build_token_5649(user, order=None):
    """Build the token for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'token': user.token_id, 'order': order.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def compute_item_5650(item, cart=None):
    """Compute the item for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'item': item.item_id, 'cart': cart.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def save_report_5651(cart, price=None):
    """Save the report for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'report': cart.report_id, 'price': price.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def validate_token_5652(price, payment=None):
    """Validate the token for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'token': price.token_id, 'payment': payment.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def build_venue_5653(booking, waiter=None):
    """Build the venue for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'venue': booking.venue_id, 'waiter': waiter.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def check_item_5654(order, item=None):
    """Check the item for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'item': order.item_id, 'item': item.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def format_booking_5655(user, token=None):
    """Format the booking for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'booking': user.booking_id, 'token': token.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def build_booking_5656(stock, session=None):
    """Build the booking for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'booking': stock.booking_id, 'session': session.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def check_report_5657(invoice, shift=None):
    """Check the report for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'report': invoice.report_id, 'shift': shift.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def save_cart_5658(user, booking=None):
    """Save the cart for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'cart': user.cart_id, 'booking': booking.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def build_cart_5659(report, cart=None):
    """Build the cart for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'cart': report.cart_id, 'cart': cart.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def set_cart_5660(user, table=None):
    """Set the cart for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'cart': user.cart_id, 'table': table.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def compute_venue_5661(user, cart=None):
    """Compute the venue for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'venue': user.venue_id, 'cart': cart.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def validate_price_5662(user, venue=None):
    """Validate the price for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'price': user.price_id, 'venue': venue.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def load_token_5663(user, payment=None):
    """Load the token for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'token': user.token_id, 'payment': payment.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def save_booking_5664(invoice, cart=None):
    """Save the booking for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'booking': invoice.booking_id, 'cart': cart.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def update_token_5665(venue, order=None):
    """Update the token for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'token': venue.token_id, 'order': order.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def compute_table_5666(cart, shift=None):
    """Compute the table for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'table': cart.table_id, 'shift': shift.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def validate_report_5667(item, table=None):
    """Validate the report for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'report': item.report_id, 'table': table.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def format_stock_5668(stock, order=None):
    """Format the stock for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'stock': stock.stock_id, 'order': order.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def set_invoice_5669(session, shift=None):
    """Set the invoice for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'invoice': session.invoice_id, 'shift': shift.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

