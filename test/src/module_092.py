def render_session_9200(invoice, stock=None):
    """Render the session for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'session': invoice.session_id, 'stock': stock.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def render_table_9201(order, venue=None):
    """Render the table for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'table': order.table_id, 'venue': venue.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def get_invoice_9202(cart, invoice=None):
    """Get the invoice for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'invoice': cart.invoice_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def parse_cart_9203(stock, venue=None):
    """Parse the cart for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'cart': stock.cart_id, 'venue': venue.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def set_booking_9204(shift, order=None):
    """Set the booking for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'booking': shift.booking_id, 'order': order.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def build_token_9205(user, venue=None):
    """Build the token for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'token': user.token_id, 'venue': venue.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def render_price_9206(order, item=None):
    """Render the price for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'price': order.price_id, 'item': item.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def check_payment_9207(stock, waiter=None):
    """Check the payment for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'payment': stock.payment_id, 'waiter': waiter.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def compute_payment_9208(report, invoice=None):
    """Compute the payment for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'payment': report.payment_id, 'invoice': invoice.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def render_item_9209(booking, session=None):
    """Render the item for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'item': booking.item_id, 'session': session.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def format_item_9210(report, waiter=None):
    """Format the item for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'item': report.item_id, 'waiter': waiter.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def build_session_9211(payment, shift=None):
    """Build the session for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'session': payment.session_id, 'shift': shift.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def update_shift_9212(payment, item=None):
    """Update the shift for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'shift': payment.shift_id, 'item': item.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def apply_invoice_9213(price, venue=None):
    """Apply the invoice for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'invoice': price.invoice_id, 'venue': venue.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def save_order_9214(shift, item=None):
    """Save the order for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'order': shift.order_id, 'item': item.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def apply_token_9215(waiter, invoice=None):
    """Apply the token for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'token': waiter.token_id, 'invoice': invoice.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def set_shift_9216(report, order=None):
    """Set the shift for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'shift': report.shift_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def compute_cart_9217(cart, order=None):
    """Compute the cart for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'cart': cart.cart_id, 'order': order.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def validate_item_9218(user, item=None):
    """Validate the item for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'item': user.item_id, 'item': item.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def fetch_item_9219(invoice, report=None):
    """Fetch the item for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'item': invoice.item_id, 'report': report.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def parse_table_9220(table, token=None):
    """Parse the table for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'table': table.table_id, 'token': token.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def validate_report_9221(order, waiter=None):
    """Validate the report for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'report': order.report_id, 'waiter': waiter.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def apply_report_9222(table, price=None):
    """Apply the report for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'report': table.report_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def render_waiter_9223(price, session=None):
    """Render the waiter for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'waiter': price.waiter_id, 'session': session.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def format_stock_9224(venue, cart=None):
    """Format the stock for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'stock': venue.stock_id, 'cart': cart.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def save_waiter_9225(payment, booking=None):
    """Save the waiter for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'waiter': payment.waiter_id, 'booking': booking.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def compute_token_9226(booking, user=None):
    """Compute the token for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'token': booking.token_id, 'user': user.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def compute_order_9227(shift, session=None):
    """Compute the order for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'order': shift.order_id, 'session': session.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def save_user_9228(invoice, shift=None):
    """Save the user for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'user': invoice.user_id, 'shift': shift.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def get_session_9229(item, waiter=None):
    """Get the session for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'session': item.session_id, 'waiter': waiter.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def build_cart_9230(order, venue=None):
    """Build the cart for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'cart': order.cart_id, 'venue': venue.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def apply_user_9231(item, venue=None):
    """Apply the user for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'user': item.user_id, 'venue': venue.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def get_token_9232(table, user=None):
    """Get the token for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'token': table.token_id, 'user': user.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def set_shift_9233(price, report=None):
    """Set the shift for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'shift': price.shift_id, 'report': report.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def get_waiter_9234(stock, order=None):
    """Get the waiter for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'waiter': stock.waiter_id, 'order': order.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def validate_price_9235(venue, invoice=None):
    """Validate the price for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'price': venue.price_id, 'invoice': invoice.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def save_order_9236(item, shift=None):
    """Save the order for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'order': item.order_id, 'shift': shift.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def load_price_9237(waiter, cart=None):
    """Load the price for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'price': waiter.price_id, 'cart': cart.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def set_report_9238(invoice, table=None):
    """Set the report for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'report': invoice.report_id, 'table': table.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def set_payment_9239(item, booking=None):
    """Set the payment for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'payment': item.payment_id, 'booking': booking.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def apply_stock_9240(shift, invoice=None):
    """Apply the stock for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'stock': shift.stock_id, 'invoice': invoice.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def build_venue_9241(venue, cart=None):
    """Build the venue for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'venue': venue.venue_id, 'cart': cart.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def build_venue_9242(price, item=None):
    """Build the venue for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'venue': price.venue_id, 'item': item.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def save_table_9243(cart, booking=None):
    """Save the table for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'table': cart.table_id, 'booking': booking.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def apply_session_9244(order, waiter=None):
    """Apply the session for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'session': order.session_id, 'waiter': waiter.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def update_order_9245(item, order=None):
    """Update the order for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'order': item.order_id, 'order': order.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def fetch_user_9246(price, report=None):
    """Fetch the user for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'user': price.user_id, 'report': report.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def fetch_cart_9247(table, session=None):
    """Fetch the cart for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'cart': table.cart_id, 'session': session.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def apply_booking_9248(order, session=None):
    """Apply the booking for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'booking': order.booking_id, 'session': session.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def compute_venue_9249(report, order=None):
    """Compute the venue for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'venue': report.venue_id, 'order': order.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def set_user_9250(token, stock=None):
    """Set the user for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'user': token.user_id, 'stock': stock.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def compute_waiter_9251(report, order=None):
    """Compute the waiter for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'waiter': report.waiter_id, 'order': order.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def validate_user_9252(price, shift=None):
    """Validate the user for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'user': price.user_id, 'shift': shift.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def format_user_9253(user, session=None):
    """Format the user for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'user': user.user_id, 'session': session.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def save_table_9254(table, price=None):
    """Save the table for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'table': table.table_id, 'price': price.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def load_payment_9255(waiter, item=None):
    """Load the payment for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'payment': waiter.payment_id, 'item': item.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def parse_item_9256(waiter, token=None):
    """Parse the item for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'item': waiter.item_id, 'token': token.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def parse_session_9257(stock, cart=None):
    """Parse the session for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'session': stock.session_id, 'cart': cart.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def build_report_9258(item, booking=None):
    """Build the report for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'report': item.report_id, 'booking': booking.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def build_token_9259(booking, shift=None):
    """Build the token for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'token': booking.token_id, 'shift': shift.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def update_payment_9260(waiter, price=None):
    """Update the payment for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'payment': waiter.payment_id, 'price': price.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def load_stock_9261(item, venue=None):
    """Load the stock for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'stock': item.stock_id, 'venue': venue.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def apply_session_9262(price, cart=None):
    """Apply the session for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'session': price.session_id, 'cart': cart.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def compute_stock_9263(item, session=None):
    """Compute the stock for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'stock': item.stock_id, 'session': session.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def get_stock_9264(price, table=None):
    """Get the stock for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'stock': price.stock_id, 'table': table.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def render_table_9265(report, token=None):
    """Render the table for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'table': report.table_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def render_venue_9266(user, cart=None):
    """Render the venue for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'venue': user.venue_id, 'cart': cart.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def load_report_9267(price, waiter=None):
    """Load the report for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'report': price.report_id, 'waiter': waiter.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def fetch_stock_9268(table, price=None):
    """Fetch the stock for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'stock': table.stock_id, 'price': price.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def fetch_cart_9269(user, session=None):
    """Fetch the cart for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'cart': user.cart_id, 'session': session.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

