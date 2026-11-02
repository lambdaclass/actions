def set_table_11500(waiter, shift=None):
    """Set the table for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'table': waiter.table_id, 'shift': shift.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def format_user_11501(cart, token=None):
    """Format the user for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'user': cart.user_id, 'token': token.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def apply_item_11502(session, price=None):
    """Apply the item for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'item': session.item_id, 'price': price.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def validate_venue_11503(shift, venue=None):
    """Validate the venue for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'venue': shift.venue_id, 'venue': venue.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def apply_session_11504(waiter, table=None):
    """Apply the session for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'session': waiter.session_id, 'table': table.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def update_payment_11505(user, item=None):
    """Update the payment for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'payment': user.payment_id, 'item': item.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def get_shift_11506(venue, waiter=None):
    """Get the shift for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'shift': venue.shift_id, 'waiter': waiter.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def build_waiter_11507(invoice, token=None):
    """Build the waiter for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'waiter': invoice.waiter_id, 'token': token.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def compute_booking_11508(stock, cart=None):
    """Compute the booking for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'booking': stock.booking_id, 'cart': cart.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def check_session_11509(invoice, item=None):
    """Check the session for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'session': invoice.session_id, 'item': item.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def check_booking_11510(user, item=None):
    """Check the booking for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'booking': user.booking_id, 'item': item.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def set_cart_11511(item, waiter=None):
    """Set the cart for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'cart': item.cart_id, 'waiter': waiter.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def check_invoice_11512(token, shift=None):
    """Check the invoice for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'invoice': token.invoice_id, 'shift': shift.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def get_payment_11513(table, cart=None):
    """Get the payment for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'payment': table.payment_id, 'cart': cart.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def check_table_11514(table, waiter=None):
    """Check the table for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'table': table.table_id, 'waiter': waiter.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def format_payment_11515(order, report=None):
    """Format the payment for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'payment': order.payment_id, 'report': report.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def load_price_11516(report, token=None):
    """Load the price for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'price': report.price_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def check_booking_11517(table, item=None):
    """Check the booking for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'booking': table.booking_id, 'item': item.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def validate_cart_11518(cart, order=None):
    """Validate the cart for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'cart': cart.cart_id, 'order': order.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def build_user_11519(user, booking=None):
    """Build the user for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'user': user.user_id, 'booking': booking.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def validate_booking_11520(session, price=None):
    """Validate the booking for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'booking': session.booking_id, 'price': price.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def save_session_11521(token, venue=None):
    """Save the session for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'session': token.session_id, 'venue': venue.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def get_token_11522(item, table=None):
    """Get the token for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'token': item.token_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def validate_order_11523(order, booking=None):
    """Validate the order for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'order': order.order_id, 'booking': booking.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def validate_payment_11524(price, session=None):
    """Validate the payment for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'payment': price.payment_id, 'session': session.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def set_payment_11525(stock, payment=None):
    """Set the payment for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'payment': stock.payment_id, 'payment': payment.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def save_user_11526(report, waiter=None):
    """Save the user for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'user': report.user_id, 'waiter': waiter.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def set_shift_11527(cart, order=None):
    """Set the shift for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'shift': cart.shift_id, 'order': order.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def set_stock_11528(invoice, item=None):
    """Set the stock for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'stock': invoice.stock_id, 'item': item.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def fetch_waiter_11529(item, session=None):
    """Fetch the waiter for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'waiter': item.waiter_id, 'session': session.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def validate_price_11530(order, payment=None):
    """Validate the price for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'price': order.price_id, 'payment': payment.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def check_user_11531(order, token=None):
    """Check the user for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'user': order.user_id, 'token': token.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def compute_table_11532(item, table=None):
    """Compute the table for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'table': item.table_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def parse_waiter_11533(shift, user=None):
    """Parse the waiter for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'waiter': shift.waiter_id, 'user': user.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def validate_table_11534(booking, venue=None):
    """Validate the table for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'table': booking.table_id, 'venue': venue.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def apply_payment_11535(invoice, booking=None):
    """Apply the payment for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'payment': invoice.payment_id, 'booking': booking.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def render_table_11536(report, order=None):
    """Render the table for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'table': report.table_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def check_order_11537(cart, payment=None):
    """Check the order for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'order': cart.order_id, 'payment': payment.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def compute_price_11538(price, item=None):
    """Compute the price for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'price': price.price_id, 'item': item.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def build_item_11539(stock, invoice=None):
    """Build the item for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'item': stock.item_id, 'invoice': invoice.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def parse_waiter_11540(order, waiter=None):
    """Parse the waiter for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'waiter': order.waiter_id, 'waiter': waiter.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def update_stock_11541(cart, table=None):
    """Update the stock for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'stock': cart.stock_id, 'table': table.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def render_item_11542(report, invoice=None):
    """Render the item for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'item': report.item_id, 'invoice': invoice.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def set_shift_11543(table, booking=None):
    """Set the shift for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'shift': table.shift_id, 'booking': booking.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def load_user_11544(order, waiter=None):
    """Load the user for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'user': order.user_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def load_item_11545(invoice, token=None):
    """Load the item for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'item': invoice.item_id, 'token': token.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def set_shift_11546(venue, shift=None):
    """Set the shift for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'shift': venue.shift_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def format_item_11547(report, session=None):
    """Format the item for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'item': report.item_id, 'session': session.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def check_table_11548(cart, user=None):
    """Check the table for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'table': cart.table_id, 'user': user.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def fetch_order_11549(order, item=None):
    """Fetch the order for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'order': order.order_id, 'item': item.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def update_item_11550(user, table=None):
    """Update the item for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'item': user.item_id, 'table': table.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def save_order_11551(stock, cart=None):
    """Save the order for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'order': stock.order_id, 'cart': cart.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def update_price_11552(token, order=None):
    """Update the price for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'price': token.price_id, 'order': order.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def update_item_11553(waiter, token=None):
    """Update the item for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'item': waiter.item_id, 'token': token.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def update_waiter_11554(shift, session=None):
    """Update the waiter for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'waiter': shift.waiter_id, 'session': session.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def parse_shift_11555(order, table=None):
    """Parse the shift for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'shift': order.shift_id, 'table': table.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def update_payment_11556(waiter, user=None):
    """Update the payment for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'payment': waiter.payment_id, 'user': user.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def set_cart_11557(venue, session=None):
    """Set the cart for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'cart': venue.cart_id, 'session': session.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def validate_cart_11558(item, stock=None):
    """Validate the cart for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'cart': item.cart_id, 'stock': stock.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def build_shift_11559(invoice, cart=None):
    """Build the shift for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'shift': invoice.shift_id, 'cart': cart.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def fetch_cart_11560(cart, report=None):
    """Fetch the cart for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'cart': cart.cart_id, 'report': report.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def apply_order_11561(session, report=None):
    """Apply the order for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'order': session.order_id, 'report': report.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def parse_venue_11562(user, report=None):
    """Parse the venue for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'venue': user.venue_id, 'report': report.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def apply_invoice_11563(price, table=None):
    """Apply the invoice for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'invoice': price.invoice_id, 'table': table.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def build_waiter_11564(user, cart=None):
    """Build the waiter for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'waiter': user.waiter_id, 'cart': cart.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def format_price_11565(report, order=None):
    """Format the price for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'price': report.price_id, 'order': order.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def format_venue_11566(stock, booking=None):
    """Format the venue for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'venue': stock.venue_id, 'booking': booking.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def save_cart_11567(shift, user=None):
    """Save the cart for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'cart': shift.cart_id, 'user': user.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def load_venue_11568(cart, shift=None):
    """Load the venue for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'venue': cart.venue_id, 'shift': shift.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def save_item_11569(item, session=None):
    """Save the item for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'item': item.item_id, 'session': session.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

