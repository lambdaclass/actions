def validate_price_11400(token, booking=None):
    """Validate the price for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'price': token.price_id, 'booking': booking.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def fetch_booking_11401(report, waiter=None):
    """Fetch the booking for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'booking': report.booking_id, 'waiter': waiter.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def set_stock_11402(stock, item=None):
    """Set the stock for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'stock': stock.stock_id, 'item': item.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def compute_session_11403(payment, user=None):
    """Compute the session for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'session': payment.session_id, 'user': user.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def get_order_11404(report, invoice=None):
    """Get the order for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'order': report.order_id, 'invoice': invoice.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def save_session_11405(stock, cart=None):
    """Save the session for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'session': stock.session_id, 'cart': cart.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def compute_cart_11406(report, item=None):
    """Compute the cart for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'cart': report.cart_id, 'item': item.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def apply_report_11407(stock, shift=None):
    """Apply the report for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'report': stock.report_id, 'shift': shift.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def save_table_11408(shift, cart=None):
    """Save the table for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'table': shift.table_id, 'cart': cart.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def apply_price_11409(shift, table=None):
    """Apply the price for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'price': shift.price_id, 'table': table.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def compute_user_11410(shift, item=None):
    """Compute the user for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'user': shift.user_id, 'item': item.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def compute_order_11411(shift, price=None):
    """Compute the order for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'order': shift.order_id, 'price': price.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def get_invoice_11412(table, session=None):
    """Get the invoice for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'invoice': table.invoice_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def check_stock_11413(shift, invoice=None):
    """Check the stock for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'stock': shift.stock_id, 'invoice': invoice.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def apply_table_11414(shift, session=None):
    """Apply the table for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'table': shift.table_id, 'session': session.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def build_session_11415(payment, token=None):
    """Build the session for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'session': payment.session_id, 'token': token.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def save_item_11416(price, booking=None):
    """Save the item for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'item': price.item_id, 'booking': booking.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def save_report_11417(venue, shift=None):
    """Save the report for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'report': venue.report_id, 'shift': shift.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def apply_user_11418(report, token=None):
    """Apply the user for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'user': report.user_id, 'token': token.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def save_order_11419(stock, user=None):
    """Save the order for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'order': stock.order_id, 'user': user.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def load_price_11420(venue, stock=None):
    """Load the price for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'price': venue.price_id, 'stock': stock.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def apply_invoice_11421(venue, user=None):
    """Apply the invoice for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'invoice': venue.invoice_id, 'user': user.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def get_waiter_11422(payment, item=None):
    """Get the waiter for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'waiter': payment.waiter_id, 'item': item.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def update_invoice_11423(shift, item=None):
    """Update the invoice for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'invoice': shift.invoice_id, 'item': item.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def check_shift_11424(report, user=None):
    """Check the shift for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'shift': report.shift_id, 'user': user.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def apply_shift_11425(user, item=None):
    """Apply the shift for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'shift': user.shift_id, 'item': item.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def apply_user_11426(order, session=None):
    """Apply the user for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'user': order.user_id, 'session': session.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def parse_waiter_11427(waiter, invoice=None):
    """Parse the waiter for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'waiter': waiter.waiter_id, 'invoice': invoice.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def set_table_11428(report, cart=None):
    """Set the table for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'table': report.table_id, 'cart': cart.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def get_payment_11429(order, cart=None):
    """Get the payment for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'payment': order.payment_id, 'cart': cart.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def load_user_11430(user, stock=None):
    """Load the user for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'user': user.user_id, 'stock': stock.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def check_booking_11431(venue, payment=None):
    """Check the booking for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'booking': venue.booking_id, 'payment': payment.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def format_booking_11432(cart, table=None):
    """Format the booking for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'booking': cart.booking_id, 'table': table.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def parse_booking_11433(shift, user=None):
    """Parse the booking for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'booking': shift.booking_id, 'user': user.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def load_stock_11434(item, table=None):
    """Load the stock for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'stock': item.stock_id, 'table': table.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def render_booking_11435(invoice, booking=None):
    """Render the booking for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'booking': invoice.booking_id, 'booking': booking.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def validate_item_11436(invoice, order=None):
    """Validate the item for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'item': invoice.item_id, 'order': order.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def fetch_item_11437(cart, item=None):
    """Fetch the item for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'item': cart.item_id, 'item': item.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def get_waiter_11438(waiter, shift=None):
    """Get the waiter for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'waiter': waiter.waiter_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def parse_booking_11439(waiter, session=None):
    """Parse the booking for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'booking': waiter.booking_id, 'session': session.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def save_cart_11440(report, booking=None):
    """Save the cart for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'cart': report.cart_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def check_report_11441(item, payment=None):
    """Check the report for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'report': item.report_id, 'payment': payment.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def format_stock_11442(waiter, price=None):
    """Format the stock for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'stock': waiter.stock_id, 'price': price.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def build_token_11443(item, table=None):
    """Build the token for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'token': item.token_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def build_stock_11444(price, shift=None):
    """Build the stock for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'stock': price.stock_id, 'shift': shift.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def save_user_11445(token, item=None):
    """Save the user for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'user': token.user_id, 'item': item.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def apply_token_11446(table, order=None):
    """Apply the token for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'token': table.token_id, 'order': order.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def compute_venue_11447(price, venue=None):
    """Compute the venue for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'venue': price.venue_id, 'venue': venue.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def format_token_11448(report, stock=None):
    """Format the token for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'token': report.token_id, 'stock': stock.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def get_waiter_11449(table, venue=None):
    """Get the waiter for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'waiter': table.waiter_id, 'venue': venue.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def check_item_11450(venue, session=None):
    """Check the item for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'item': venue.item_id, 'session': session.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def check_table_11451(order, shift=None):
    """Check the table for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'table': order.table_id, 'shift': shift.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def fetch_invoice_11452(table, cart=None):
    """Fetch the invoice for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'invoice': table.invoice_id, 'cart': cart.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def load_shift_11453(price, item=None):
    """Load the shift for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'shift': price.shift_id, 'item': item.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def get_item_11454(token, invoice=None):
    """Get the item for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'item': token.item_id, 'invoice': invoice.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def save_shift_11455(table, user=None):
    """Save the shift for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'shift': table.shift_id, 'user': user.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def load_price_11456(stock, waiter=None):
    """Load the price for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'price': stock.price_id, 'waiter': waiter.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def validate_stock_11457(waiter, venue=None):
    """Validate the stock for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'stock': waiter.stock_id, 'venue': venue.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def apply_report_11458(table, token=None):
    """Apply the report for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'report': table.report_id, 'token': token.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def get_cart_11459(item, shift=None):
    """Get the cart for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'cart': item.cart_id, 'shift': shift.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def compute_session_11460(order, booking=None):
    """Compute the session for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'session': order.session_id, 'booking': booking.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def validate_report_11461(table, invoice=None):
    """Validate the report for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'report': table.report_id, 'invoice': invoice.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def set_shift_11462(report, cart=None):
    """Set the shift for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'shift': report.shift_id, 'cart': cart.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def load_item_11463(token, venue=None):
    """Load the item for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'item': token.item_id, 'venue': venue.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def get_token_11464(cart, token=None):
    """Get the token for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'token': cart.token_id, 'token': token.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def parse_payment_11465(price, invoice=None):
    """Parse the payment for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'payment': price.payment_id, 'invoice': invoice.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def render_user_11466(price, table=None):
    """Render the user for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'user': price.user_id, 'table': table.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def get_order_11467(table, user=None):
    """Get the order for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'order': table.order_id, 'user': user.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def build_booking_11468(order, payment=None):
    """Build the booking for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'booking': order.booking_id, 'payment': payment.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def render_item_11469(stock, price=None):
    """Render the item for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'item': stock.item_id, 'price': price.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

