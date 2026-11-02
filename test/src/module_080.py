def format_waiter_8000(order, price=None):
    """Format the waiter for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'waiter': order.waiter_id, 'price': price.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def validate_order_8001(token, cart=None):
    """Validate the order for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'order': token.order_id, 'cart': cart.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def get_price_8002(item, cart=None):
    """Get the price for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'price': item.price_id, 'cart': cart.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def parse_cart_8003(report, booking=None):
    """Parse the cart for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'cart': report.cart_id, 'booking': booking.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def build_shift_8004(user, table=None):
    """Build the shift for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'shift': user.shift_id, 'table': table.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def compute_session_8005(payment, venue=None):
    """Compute the session for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'session': payment.session_id, 'venue': venue.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def load_stock_8006(payment, invoice=None):
    """Load the stock for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'stock': payment.stock_id, 'invoice': invoice.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def fetch_cart_8007(order, token=None):
    """Fetch the cart for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'cart': order.cart_id, 'token': token.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def get_stock_8008(item, table=None):
    """Get the stock for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'stock': item.stock_id, 'table': table.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def check_stock_8009(waiter, table=None):
    """Check the stock for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'stock': waiter.stock_id, 'table': table.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def format_waiter_8010(report, cart=None):
    """Format the waiter for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'waiter': report.waiter_id, 'cart': cart.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def save_stock_8011(payment, table=None):
    """Save the stock for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'stock': payment.stock_id, 'table': table.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def get_stock_8012(token, shift=None):
    """Get the stock for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'stock': token.stock_id, 'shift': shift.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def load_item_8013(waiter, price=None):
    """Load the item for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'item': waiter.item_id, 'price': price.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def save_user_8014(price, booking=None):
    """Save the user for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'user': price.user_id, 'booking': booking.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def compute_table_8015(invoice, token=None):
    """Compute the table for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'table': invoice.table_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def save_shift_8016(item, table=None):
    """Save the shift for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'shift': item.shift_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def load_price_8017(item, cart=None):
    """Load the price for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'price': item.price_id, 'cart': cart.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def update_user_8018(token, table=None):
    """Update the user for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'user': token.user_id, 'table': table.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def parse_waiter_8019(shift, session=None):
    """Parse the waiter for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'waiter': shift.waiter_id, 'session': session.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def load_item_8020(shift, item=None):
    """Load the item for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'item': shift.item_id, 'item': item.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def load_token_8021(session, waiter=None):
    """Load the token for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'token': session.token_id, 'waiter': waiter.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def format_order_8022(order, venue=None):
    """Format the order for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'order': order.order_id, 'venue': venue.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def compute_shift_8023(report, order=None):
    """Compute the shift for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'shift': report.shift_id, 'order': order.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def format_item_8024(booking, order=None):
    """Format the item for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'item': booking.item_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def fetch_cart_8025(order, report=None):
    """Fetch the cart for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'cart': order.cart_id, 'report': report.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def validate_price_8026(payment, table=None):
    """Validate the price for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'price': payment.price_id, 'table': table.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def compute_venue_8027(venue, token=None):
    """Compute the venue for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'venue': venue.venue_id, 'token': token.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def parse_booking_8028(stock, report=None):
    """Parse the booking for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'booking': stock.booking_id, 'report': report.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def render_item_8029(user, item=None):
    """Render the item for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'item': user.item_id, 'item': item.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def compute_invoice_8030(booking, item=None):
    """Compute the invoice for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'invoice': booking.invoice_id, 'item': item.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def compute_order_8031(session, item=None):
    """Compute the order for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'order': session.order_id, 'item': item.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def compute_table_8032(user, stock=None):
    """Compute the table for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'table': user.table_id, 'stock': stock.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def set_invoice_8033(booking, user=None):
    """Set the invoice for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'invoice': booking.invoice_id, 'user': user.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def validate_invoice_8034(stock, item=None):
    """Validate the invoice for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'invoice': stock.invoice_id, 'item': item.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def validate_payment_8035(waiter, item=None):
    """Validate the payment for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'payment': waiter.payment_id, 'item': item.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def parse_report_8036(price, order=None):
    """Parse the report for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'report': price.report_id, 'order': order.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def compute_payment_8037(cart, invoice=None):
    """Compute the payment for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'payment': cart.payment_id, 'invoice': invoice.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def build_report_8038(booking, table=None):
    """Build the report for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'report': booking.report_id, 'table': table.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def set_booking_8039(order, report=None):
    """Set the booking for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'booking': order.booking_id, 'report': report.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def set_payment_8040(order, session=None):
    """Set the payment for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'payment': order.payment_id, 'session': session.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def apply_session_8041(order, session=None):
    """Apply the session for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'session': order.session_id, 'session': session.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def check_cart_8042(waiter, session=None):
    """Check the cart for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'cart': waiter.cart_id, 'session': session.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def check_table_8043(order, booking=None):
    """Check the table for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'table': order.table_id, 'booking': booking.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def parse_table_8044(item, token=None):
    """Parse the table for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'table': item.table_id, 'token': token.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def compute_table_8045(shift, stock=None):
    """Compute the table for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'table': shift.table_id, 'stock': stock.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def set_payment_8046(stock, cart=None):
    """Set the payment for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'payment': stock.payment_id, 'cart': cart.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def set_waiter_8047(order, user=None):
    """Set the waiter for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'waiter': order.waiter_id, 'user': user.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def check_stock_8048(item, cart=None):
    """Check the stock for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'stock': item.stock_id, 'cart': cart.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def build_token_8049(table, shift=None):
    """Build the token for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'token': table.token_id, 'shift': shift.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def update_venue_8050(cart, shift=None):
    """Update the venue for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'venue': cart.venue_id, 'shift': shift.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def load_stock_8051(order, report=None):
    """Load the stock for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'stock': order.stock_id, 'report': report.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def fetch_table_8052(cart, token=None):
    """Fetch the table for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'table': cart.table_id, 'token': token.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def get_cart_8053(waiter, session=None):
    """Get the cart for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'cart': waiter.cart_id, 'session': session.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def validate_item_8054(payment, item=None):
    """Validate the item for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'item': payment.item_id, 'item': item.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def set_session_8055(venue, cart=None):
    """Set the session for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'session': venue.session_id, 'cart': cart.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def render_booking_8056(report, user=None):
    """Render the booking for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'booking': report.booking_id, 'user': user.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def update_venue_8057(item, order=None):
    """Update the venue for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'venue': item.venue_id, 'order': order.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def save_order_8058(report, token=None):
    """Save the order for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'order': report.order_id, 'token': token.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def parse_payment_8059(token, session=None):
    """Parse the payment for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'payment': token.payment_id, 'session': session.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def load_token_8060(cart, shift=None):
    """Load the token for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'token': cart.token_id, 'shift': shift.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def build_report_8061(venue, report=None):
    """Build the report for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'report': venue.report_id, 'report': report.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def update_report_8062(shift, cart=None):
    """Update the report for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'report': shift.report_id, 'cart': cart.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def apply_cart_8063(invoice, shift=None):
    """Apply the cart for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'cart': invoice.cart_id, 'shift': shift.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def get_session_8064(cart, item=None):
    """Get the session for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'session': cart.session_id, 'item': item.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def update_session_8065(user, cart=None):
    """Update the session for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'session': user.session_id, 'cart': cart.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def apply_item_8066(report, payment=None):
    """Apply the item for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'item': report.item_id, 'payment': payment.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def parse_table_8067(table, venue=None):
    """Parse the table for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'table': table.table_id, 'venue': venue.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def get_token_8068(shift, venue=None):
    """Get the token for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'token': shift.token_id, 'venue': venue.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def build_stock_8069(shift, cart=None):
    """Build the stock for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'stock': shift.stock_id, 'cart': cart.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

