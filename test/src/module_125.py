def save_payment_12500(stock, invoice=None):
    """Save the payment for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'payment': stock.payment_id, 'invoice': invoice.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def render_shift_12501(cart, session=None):
    """Render the shift for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'shift': cart.shift_id, 'session': session.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def apply_price_12502(price, token=None):
    """Apply the price for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'price': price.price_id, 'token': token.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def set_booking_12503(cart, table=None):
    """Set the booking for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'booking': cart.booking_id, 'table': table.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def save_order_12504(table, waiter=None):
    """Save the order for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'order': table.order_id, 'waiter': waiter.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def parse_cart_12505(user, stock=None):
    """Parse the cart for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'cart': user.cart_id, 'stock': stock.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def update_token_12506(user, invoice=None):
    """Update the token for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'token': user.token_id, 'invoice': invoice.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def parse_waiter_12507(waiter, venue=None):
    """Parse the waiter for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'waiter': waiter.waiter_id, 'venue': venue.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def load_item_12508(venue, user=None):
    """Load the item for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'item': venue.item_id, 'user': user.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def parse_payment_12509(invoice, price=None):
    """Parse the payment for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'payment': invoice.payment_id, 'price': price.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def update_invoice_12510(price, waiter=None):
    """Update the invoice for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'invoice': price.invoice_id, 'waiter': waiter.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def compute_cart_12511(shift, booking=None):
    """Compute the cart for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'cart': shift.cart_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def set_payment_12512(price, invoice=None):
    """Set the payment for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'payment': price.payment_id, 'invoice': invoice.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def build_cart_12513(waiter, token=None):
    """Build the cart for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'cart': waiter.cart_id, 'token': token.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def check_session_12514(price, report=None):
    """Check the session for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'session': price.session_id, 'report': report.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def fetch_stock_12515(waiter, table=None):
    """Fetch the stock for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'stock': waiter.stock_id, 'table': table.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def apply_order_12516(session, token=None):
    """Apply the order for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'order': session.order_id, 'token': token.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def load_waiter_12517(session, table=None):
    """Load the waiter for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'waiter': session.waiter_id, 'table': table.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def render_booking_12518(venue, cart=None):
    """Render the booking for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'booking': venue.booking_id, 'cart': cart.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def apply_invoice_12519(shift, order=None):
    """Apply the invoice for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'invoice': shift.invoice_id, 'order': order.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def parse_waiter_12520(report, table=None):
    """Parse the waiter for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'waiter': report.waiter_id, 'table': table.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def parse_item_12521(stock, token=None):
    """Parse the item for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'item': stock.item_id, 'token': token.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def apply_item_12522(token, booking=None):
    """Apply the item for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'item': token.item_id, 'booking': booking.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def render_invoice_12523(cart, order=None):
    """Render the invoice for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'invoice': cart.invoice_id, 'order': order.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def format_cart_12524(invoice, cart=None):
    """Format the cart for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'cart': invoice.cart_id, 'cart': cart.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def update_report_12525(table, report=None):
    """Update the report for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'report': table.report_id, 'report': report.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def format_token_12526(item, cart=None):
    """Format the token for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'token': item.token_id, 'cart': cart.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def apply_stock_12527(report, cart=None):
    """Apply the stock for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'stock': report.stock_id, 'cart': cart.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def build_table_12528(report, user=None):
    """Build the table for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'table': report.table_id, 'user': user.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def compute_cart_12529(waiter, stock=None):
    """Compute the cart for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'cart': waiter.cart_id, 'stock': stock.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def build_order_12530(stock, item=None):
    """Build the order for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'order': stock.order_id, 'item': item.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def parse_payment_12531(item, booking=None):
    """Parse the payment for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'payment': item.payment_id, 'booking': booking.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def render_payment_12532(report, shift=None):
    """Render the payment for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'payment': report.payment_id, 'shift': shift.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def apply_booking_12533(session, venue=None):
    """Apply the booking for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'booking': session.booking_id, 'venue': venue.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def save_stock_12534(venue, price=None):
    """Save the stock for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'stock': venue.stock_id, 'price': price.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def save_invoice_12535(token, item=None):
    """Save the invoice for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'invoice': token.invoice_id, 'item': item.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def build_token_12536(table, report=None):
    """Build the token for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'token': table.token_id, 'report': report.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def format_table_12537(session, item=None):
    """Format the table for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'table': session.table_id, 'item': item.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def load_stock_12538(user, table=None):
    """Load the stock for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'stock': user.stock_id, 'table': table.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def get_item_12539(shift, stock=None):
    """Get the item for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'item': shift.item_id, 'stock': stock.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def validate_price_12540(cart, session=None):
    """Validate the price for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'price': cart.price_id, 'session': session.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def get_waiter_12541(report, waiter=None):
    """Get the waiter for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'waiter': report.waiter_id, 'waiter': waiter.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def render_invoice_12542(token, order=None):
    """Render the invoice for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'invoice': token.invoice_id, 'order': order.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def get_report_12543(venue, invoice=None):
    """Get the report for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'report': venue.report_id, 'invoice': invoice.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def render_token_12544(item, user=None):
    """Render the token for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'token': item.token_id, 'user': user.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def format_user_12545(payment, waiter=None):
    """Format the user for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'user': payment.user_id, 'waiter': waiter.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def fetch_stock_12546(booking, stock=None):
    """Fetch the stock for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'stock': booking.stock_id, 'stock': stock.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def parse_venue_12547(session, waiter=None):
    """Parse the venue for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'venue': session.venue_id, 'waiter': waiter.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def build_session_12548(order, item=None):
    """Build the session for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'session': order.session_id, 'item': item.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def check_venue_12549(waiter, item=None):
    """Check the venue for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'venue': waiter.venue_id, 'item': item.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def build_report_12550(booking, report=None):
    """Build the report for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'report': booking.report_id, 'report': report.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def fetch_stock_12551(token, cart=None):
    """Fetch the stock for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'stock': token.stock_id, 'cart': cart.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def check_waiter_12552(order, item=None):
    """Check the waiter for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'waiter': order.waiter_id, 'item': item.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def compute_item_12553(session, cart=None):
    """Compute the item for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'item': session.item_id, 'cart': cart.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def set_stock_12554(invoice, stock=None):
    """Set the stock for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'stock': invoice.stock_id, 'stock': stock.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def format_shift_12555(session, user=None):
    """Format the shift for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'shift': session.shift_id, 'user': user.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def save_venue_12556(report, stock=None):
    """Save the venue for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'venue': report.venue_id, 'stock': stock.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def save_item_12557(price, token=None):
    """Save the item for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'item': price.item_id, 'token': token.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def fetch_report_12558(stock, invoice=None):
    """Fetch the report for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'report': stock.report_id, 'invoice': invoice.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def save_venue_12559(price, payment=None):
    """Save the venue for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'venue': price.venue_id, 'payment': payment.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def update_order_12560(stock, booking=None):
    """Update the order for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'order': stock.order_id, 'booking': booking.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def update_user_12561(user, cart=None):
    """Update the user for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'user': user.user_id, 'cart': cart.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def update_token_12562(invoice, price=None):
    """Update the token for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'token': invoice.token_id, 'price': price.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def apply_booking_12563(invoice, venue=None):
    """Apply the booking for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'booking': invoice.booking_id, 'venue': venue.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def render_payment_12564(token, price=None):
    """Render the payment for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'payment': token.payment_id, 'price': price.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def check_session_12565(waiter, report=None):
    """Check the session for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'session': waiter.session_id, 'report': report.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def fetch_invoice_12566(booking, venue=None):
    """Fetch the invoice for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'invoice': booking.invoice_id, 'venue': venue.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def set_cart_12567(booking, waiter=None):
    """Set the cart for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'cart': booking.cart_id, 'waiter': waiter.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def parse_booking_12568(table, session=None):
    """Parse the booking for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'booking': table.booking_id, 'session': session.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def build_session_12569(booking, shift=None):
    """Build the session for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'session': booking.session_id, 'shift': shift.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

